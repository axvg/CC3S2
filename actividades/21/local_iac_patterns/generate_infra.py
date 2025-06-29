#!/usr/bin/env python3
"""
Punto de entrada que une todos los patrones para generar una configuración
Terraform completamente local en formato JSON.

El archivo resultante puede aplicarse con:

    $ cd terraform
    $ terraform init
    $ terraform apply

No se requieren credenciales de nube, demonio de Docker, ni dependencias externas.
"""

import os
import shutil
from iac_patterns.builder import InfrastructureBuilder
from iac_patterns.singleton import ConfigSingleton
from iac_patterns.factory import NullResourceFactory, TimestampedNullResourceFactory
from iac_patterns.prototype import ResourcePrototype


def validate_singleton():
    c1 = ConfigSingleton("dev")
    created_at = c1.created_at
    c1.set("clave", "valor")
    c1.reset()
    assert c1.settings == {}, "Los settings no se vaciaron"
    assert c1.created_at == created_at, "La fecha de creacion cambio"


def add_timestamped_resource(builder: InfrastructureBuilder):
    builder._module.add(TimestampedNullResourceFactory.create(
        "recurso_con_fecha", fmt="%Y%m%d"))


def add_prototype_with_local_file(builder: InfrastructureBuilder):
    def add_welcome_file_mutator(block: dict):
        res_block = block["resource"]["null_resource"]
        res_name = list(res_block.keys())[0]
        res_block[res_name]["triggers"]["welcome"] = "mutador"

        block["resource"]["local_file"] = {
            "welcome_txt": {
                "content": "generado por el prototipo",
                "filename": "${path.module}/bienvenida.txt"
            }
        }

    proto = ResourcePrototype(
        NullResourceFactory.create("recurso_base_para_clonar"))
    clon_con_fichero = proto.clone(add_welcome_file_mutator)
    builder._module.add(clon_con_fichero.data)


def add_submodules_with_builder(builder: InfrastructureBuilder, modules_dir: str):
    builder.build_group(name="mi_grupo_network",
                        size=2, source_dir=modules_dir)
    builder.build_group(name="mi_grupo_app", size=3, source_dir=modules_dir)


def main() -> None:
    # Inicializa una configuración global única para el entorno "local-dev"
    config = ConfigSingleton(env_name="desarrollo-local")
    config.set("proyecto", "patrones_iac_locales")

    # Construye la infraestructura usando el nombre de entorno desde la configuración global
    builder = InfrastructureBuilder(env_name=config.env_name)

    # Construye 15 recursos null ficticios para demostrar escalabilidad (>1000 líneas en total)
    builder.build_null_fleet(count=15)

    # Agrega un recurso final personalizado con una nota descriptiva
    builder.add_custom_resource(
        name="finalizador",
        triggers={"nota": "Recurso compuesto generado dinámicamente en tiempo de ejecución"}
    )

    # Exporta el resultado a un archivo Terraform JSON en el directorio especificado
    builder.export(path=os.path.join("terraform", "main.tf.json"))


# Ejecuta la función principal si el archivo se ejecuta directamente
if __name__ == "__main__":
    main()
