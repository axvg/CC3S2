### Actividad: Patrones para módulos de infraestructura

En esta actividad: 
1. Profundizaremos en los patrones **Singleton**, **Factory**, **Prototype**, **Composite** y **Builder** aplicados a IaC.
2. Analizaremos y extenderemos el código Python existente para generar configuraciones Terraform locales.
3. Diseñaremos soluciones propias, escribir tests y evaluar escalabilidad.

<details>
<summary><strong>Fase 0: Preparación</strong></summary>

Utiliza para esta actividad el siguiente [proyecto](https://github.com/kapumota/DS/tree/main/2025-1/local_iac_patterns) como referencia.

1. **Configura** el entorno virtual:

   ```bash
   cd local_iac_patterns
   python -m venv .venv && source .venv/bin/activate
   pip install --upgrade pip
   ```
2. **Genera** la infraestructura base y valida:

   ```bash
   python generate_infra.py
   cd terraform
   terraform init
   terraform validate
   ```
3. **Inspecciona** `terraform/main.tf.json` para ver los bloques `null_resource` generados.

</details>

<details>
<summary><strong>Fase 1: Exploración y análisis</strong></summary>

Para cada patrón, localiza el archivo correspondiente y responde (los códigos son de referencia):

##### 1. Singleton

```python
# singleton.py
import threading
from datetime import datetime

class SingletonMeta(type):
    _instances: dict = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class ConfigSingleton(metaclass=SingletonMeta):
    def __init__(self, env_name: str):
        self.env_name = env_name
        self.settings: dict = {}
        self.created_at: str = datetime.utcnow().isoformat()
```

* **Tarea**: Explica cómo `SingletonMeta` garantiza una sola instancia y el rol del `lock`.

#### 2. Factory

```python
# factory.py
import uuid
from datetime import datetime

class NullResourceFactory:
    @staticmethod
    def create(name: str, triggers: dict = None) -> dict:
        triggers = triggers or {
            "factory_uuid": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat()
        }
        return {
            "resource": {
                "null_resource": {
                    name: {"triggers": triggers}
                }
            }
        }
```

* **Tarea**: Detalla cómo la fábrica encapsula la creación de `null_resource` y el propósito de sus `triggers`.

#### 3. Prototype

```python
# prototype.py
from copy import deepcopy
from typing import Callable

class ResourcePrototype:
    def __init__(self, template: dict):
        self.template = template

    def clone(self, mutator: Callable[[dict], None]) -> dict:
        new_copy = deepcopy(self.template)
        mutator(new_copy)
        return new_copy
```

* **Tarea**: Dibuja un diagrama UML del proceso de clonación profunda y explica cómo el **mutator** permite personalizar cada instancia.

#### 4. Composite

```python
# composite.py
from typing import List, Dict

class CompositeModule:
    def __init__(self):
        self.children: List[Dict] = []

    def add(self, block: Dict):
        self.children.append(block)

    def export(self) -> Dict:
        merged: Dict = {"resource": {}}
        for child in self.children:
            # Imagina que unimos dicts de forma recursiva
            for rtype, resources in child["resource"].items():
                merged["resource"].setdefault(rtype, {}).update(resources)
        return merged
```

* **Tarea**: Describe cómo `CompositeModule` agrupa múltiples bloques en un solo JSON válido para Terraform.

#### 5. Builder

```python
# builder.py
import json
from composite import CompositeModule
from factory import NullResourceFactory
from prototype import ResourcePrototype

class InfrastructureBuilder:
    def __init__(self):
        self.module = CompositeModule()

    def build_null_fleet(self, count: int):
        base = NullResourceFactory.create("app")
        proto = ResourcePrototype(base)
        for i in range(count):
            def mutator(block):
                # Renombrar recurso "app" a "app_<i>"
                res = block["resource"]["null_resource"].pop("app")
                block["resource"]["null_resource"][f"app_{i}"] = res
            self.module.add(proto.clone(mutator))
        return self

    def export(self, path: str = "terraform/main.tf.json"):
        with open(path, "w") as f:
            json.dump(self.module.export(), f, indent=2)
```

* **Tarea**: Explica cómo `InfrastructureBuilder` orquesta Factory -> Prototype -> Composite y genera el archivo JSON final.

> **Entregable fase 1**: Documentocon fragmentos de código destacados, explicación de cada patrón y un diagrama UML simplificado.

</details>

### Fase 1: Analisis de Patrones

#### 1. Singleton

La `SingletonMeta` se asegura de que solo exista una instancia de `ConfigSingleton` usando un diccionario `_instances` para guardar la primera que se crea. Si se intenta crear otra, devuelve la que ya existe. El `_lock` es para evitar problemas si varios hilos intentan crear la instancia al mismo tiempo, asegurando que solo uno pueda hacerlo.

#### 2. Factory

La `NullResourceFactory` hace mas facil crear recursos `null_resource` porque no tienes que escribir todo el JSON manualmente sino con script. Se invoca a `create` y se obtiene el archivo `tf.json` que se usa para el ciclo `plan`, `apply` con terraform. Los `triggers` le dicen a Terraform cuando tiene que recrear el recurso, y la factory les pone un `uuid` y un `timestamp` para que cada recurso sea unico.

#### 3. Prototype

`ResourcePrototype` sirve para clonar objetos. Con `deepcopy` para que la copia sea independiente del original. El `mutator` es una funcion que le pasas para hacerle cambios al clon justo despues de crearlo, lo que permite personalizarlo sin tocar el prototipo.

#### 4. Composite

El `CompositeModule` es para agrupar varios recursos de Terraform como uno solo. Los guarda en un array y con `export` los junta todos en un unico archivo `tf.json` que Terraform usa para levantar recursos.

#### 5. Builder

La clase `InfrastructureBuilder` organiza a los otros patrones para construir el archivo de configuracion final. Usa la `Factory` para crear un recurso base, lo convierte en un `Prototype` para clonarlo, personaliza cada clon con un `mutator` y los agrupa con el `Composite`. Tiene en cuenta las dependencias entre los modulos usados anteriormente con esto crea el archivo `tf.json` final.

<details>
<summary><strong>Fase 2: Ejercicios prácticos</strong></summary>

Extiende el código base en una rama nueva por ejercicio:

#### Ejercicio 2.1: Extensión del Singleton

* **Objetivo**: Añadir un método `reset()` que limpie `settings` pero mantenga `created_at`.
* **Código de partida**:

  ```python
  class ConfigSingleton(metaclass=SingletonMeta):
      # ...
      def reset(self):
          # TODO: implementar
  ```
* **Validación**:

  ```python
  c1 = ConfigSingleton("dev")
  created = c1.created_at
  c1.settings["x"] = 1
  c1.reset()
  assert c1.settings == {}
  assert c1.created_at == created
  ```

#### Ejercicio 2.2: Variación de la Factory

* **Objetivo**: Crear `TimestampedNullResourceFactory` que acepte un `fmt: str`.
* **Esqueleto**:

  ```python
  class TimestampedNullResourceFactory(NullResourceFactory):
      @staticmethod
      def create(name: str, fmt: str) -> dict:
          ts = datetime.utcnow().strftime(fmt)
          # TODO: usar ts en triggers
  ```
* **Prueba**: Genera recurso con formato `'%Y%m%d'` y aplica `terraform plan`.

#### Ejercicio 2.3: Mutaciones avanzadas con Prototype

* **Objetivo**: Clonar un prototipo y, en el mutator, añadir un bloque `local_file`.
* **Referencia**:

  ```python
  def add_welcome_file(block: dict):
      block["resource"]["null_resource"]["app_0"]["triggers"]["welcome"] = "¡Hola!"
      block["resource"]["local_file"] = {
          "welcome_txt": {
              "content": "Bienvenido",
              "filename": "${path.module}/bienvenida.txt"
          }
      }
  ```
* **Resultado**: Al `terraform apply`, genera `bienvenida.txt`.

#### Ejercicio 2.4: Submódulos con Composite

* **Objetivo**: Modificar `CompositeModule.add()` para soportar submódulos:

  ```python
  # composite.py (modificado)
  def export(self):
      merged = {"module": {}, "resource": {}}
      for child in self.children:
          if "module" in child:
              merged["module"].update(child["module"])
          # ...
  ```
* **Tarea**: Crea dos submódulos "network" y "app" en la misma export y valida con Terraform.

#### Ejercicio 2.5: Builder personalizado

* **Objetivo**: En `InfrastructureBuilder`, implementar `build_group(name: str, size: int)`:

  ```python
  def build_group(self, name: str, size: int):
      base = NullResourceFactory.create(name)
      proto = ResourcePrototype(base)
      group = CompositeModule()
      for i in range(size):
          def mut(block):  # renombrar
              res = block["resource"]["null_resource"].pop(name)
              block["resource"]["null_resource"][f"{name}_{i}"] = res
          group.add(proto.clone(mut))
      self.module.add({"module": {name: group.export()}})
      return self
  ```
* **Validación**: Exportar a JSON y revisar anidamiento `module -> <name> -> resource`.

> **Entregable Fase 2**: Ramas Git con cada ejercicio, código modificado y logs de `terraform plan`/`apply`.

</details>

#### 2.1 Extension del Singleton

Se añadio un metodo `reset()` a la clase `ConfigSingleton`. Este metodo usa `self.settings.clear()` para vaciar el diccionario de configuraciones sin afectar otros atributos como `created_at`. La prueba de validacion confirma que despues de llamar a `reset`, `settings` esta vacio pero la fecha de creacion se mantiene igual.

#### 2.2 Variacion de la Factory

Se creo una nueva clase `TimestampedNullResourceFactory` que hereda de la original. El nuevo metodo `create` acepta un parametro `fmt` para formatear la fecha. Llama al `create` de la clase padre para tener la estructura base y luego sobreescribe el valor del `timestamp` con la fecha formateada.

#### 2.3 Mutaciones avanzadas con Prototype

Se crea la funcion externa `mutator` llamada `add_welcome_file`. Esta funcion modifica los `triggers` del recurso clonado tambien añade un bloque de recurso nuevo (`local_file`). Con esto se muestra como el prototipo permite agregar complejidad a los clones sin alterar el original.

#### 2.4 Submodulos con Composite

Se modifico el metodo `export` de `CompositeModule`. Ahora ademas de juntar los `resource`, tambien busca una clave `module` en sus hijos. Si la encuentra, junta esos bloques en una seccion de modulos. Esto permite que el `Composite` pueda agrupar no solo recursos individuales sino tambien modulos enteros haciendo la estructura mas organizada.

#### 2.5 Builder personalizado

Se implemento el metodo `build_group` en el `InfrastructureBuilder`. Este metodo crea un `CompositeModule` temporal para agrupar un conjunto de recursos. Despues de clonar y mutar los recursos para ese grupo en lugar de añadirlos directamente al modulo principal, los envuelve en un diccionario bajo la clave `module`. Esto hace uso de la nueva capacidad del `Composite` para anidar modulos creando una jerarquia mas clara en el `tf.json` final.

<details>
<summary><strong>Fase 3: Desafíos teórico-prácticos</strong></summary>

#### 3.1 Comparativa Factory vs Prototype

* **Contenido** (\~300 palabras): cuándo elegir cada patrón para IaC, costes de serialización profundas vs creación directa y mantenimiento.

#### 3.2 Patrones avanzados: Adapter (código de referencia)

* **Implementación**:

  ```python
  # adapter.py
  class MockBucketAdapter:
      def __init__(self, null_block: dict):
          self.null = null_block

      def to_bucket(self) -> dict:
          # Mapear triggers a parámetros de bucket simulado
          name = list(self.null["resource"]["null_resource"].keys())[0]
          return {
              "resource": {
                  "mock_cloud_bucket": {
                      name: {"name": name, **self.null["resource"]["null_resource"][name]["triggers"]}
                  }
              }
          }
  ```
* **Prueba**: Inserta en builder y exporta un recurso `mock_cloud_bucket`.

#### 3.3 Tests automatizados con pytest

* **Ejemplos**:

  ```python
  def test_singleton_meta():
      a = ConfigSingleton("X"); b = ConfigSingleton("Y")
      assert a is b

  def test_prototype_clone_independent():
      proto = ResourcePrototype(NullResourceFactory.create("app"))
      c1 = proto.clone(lambda b: b.__setitem__("foo", 1))
      c2 = proto.clone(lambda b: b.__setitem__("bar", 2))
      assert "foo" not in c2 and "bar" not in c1
  ```

#### 3.4 Escalabilidad de JSON

* **Tarea**: Mide tamaño de `terraform/main.tf.json` para `build_null_fleet(15)` vs `(150)`.
* **Discusión**: impacto en CI/CD, posibles estrategias de fragmentación.

#### 3.5 Integración con Terraform Cloud (opcional)

* **Esquema**: `builder.export_to_cloud(workspace)` usando API HTTP.
* **Diagrama**: Flujo desde `generate_infra.py` -> `terraform login` -> `apply`.

> **Entrega final**:
>
> * Informe comparativo y código de Adapter.
> * Suite de tests.
> * Análisis de escalabilidad.
> * (Opcional) Documento con flujo de integración a Terraform Cloud.

</details>

#### 3.1 Comparativa Factory vs Prototype

El patron **Factory** desacopla al cliente del proceso de instanciacion de un objeto. Se invoca un metodo que retorna una nueva instancia, ocultando la logica de creacion. Es optimo para la generacion de recursos con una configuracion estandarizada donde cada instancia debe ser nueva e independiente.

El patron **Prototype**, en cambio, crea nuevos objetos clonando una instancia existente. Su principal ventaja es el rendimiento cuando la instanciacion de un objeto es costosa. En lugar de reconstruir el estado del objeto desde cero, se copia un estado ya configurado. La personalizacion se logra post-clonacion mediante un `mutator`.

La eleccion depende del costo de creacion vs el costo de clonacion. Para objetos simples, una Factory es mas directa. Para objetos complejos con estados iniciales costosos de construir, el Prototype es mas eficiente, aunque se debe considerar el overhead del `deepcopy`.

#### 3.2 y 3.3 Implementacion de Adapter y Tests

Se creo el archivo `iac_patterns/adapter.py` para implementar el patron Adapter. Este adapta un `null_resource` para que se comporte como un `mock_cloud_bucket`, mapeando sus `triggers` a los atributos del bucket.

Ademas, se creo el directorio `tests/` con el archivo `test_patterns.py`. Este archivo contiene tests para `Singleton`, `Prototype` y `Adapter` usando `pytest`.

#### 3.4 Escalabilidad de JSON y Estrategias de Fragmentacion

Al generar la infraestructura con 15 y 150 recursos, se observa un crecimiento lineal en el tamaño del archivo `main.tf.json`.

Un archivo JSON de 150  hara que la velocidad del ciclo de CI/CD sea baja. La generacion del archivo toma mas tiempo y los comandos de Terraform como `plan` y `apply` se vuelven muy lentos porque tienen que procesar un unico archivo grande. Revisar cambios en un pull request tambien se volveria una tarea mas grande.

La solucion es usar **modulos** como se hizo en la Fase 2. En lugar de tener un solo archivo gigante, se divide la infraestructura en partes logicas (modulos), cada una con su propio archivo de configuracion. El archivo principal solo contiene referencias a estos modulos. Esto hace que el codigo sea mas organizado, mantenible y escalable. Los `plan` y `apply` se pueden incluso ejecutar por modulo, acelerando el proceso de despliegue y CI.