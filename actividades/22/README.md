### Actividad: Patrones de dependencias y módulos en IaC con Terraform y Python

#### Objetivos

1. Comprender y aplicar patrones de dependencia (unidireccional, inyección de dependencias, facade, adaptador, mediador).
2. Explorar distintos esquemas de organización de repositorios (mono-repositorio vs multi-repositorio).
3. Implementar control de versiones, liberación y publicación de módulos Terraform.
4. Ejecutar, probar y compartir módulos de manera local y remota.

#### Pre-requisitos

* Utiliza el siguiente [proyecto](https://github.com/kapumota/DS/tree/main/2025-1/Patrones_dependencias_infraestructura) dado y las lecturas 27->29 del curso.
* Tener instalados:

  * Terraform (>= 1.0)
  * Python 3.8+
  * `make`

<details>
<summary><strong>Fase 1: Relaciones unidireccionales</strong></summary>

1. **Inspección**

   * Explora `network/network.tf.json` y `main.tf.json`.
   * Identifica recursos y sus dependencias implícitas (`depends_on`).

2. **Ejercicio práctico**

   * Ejecuta:

     ```bash
     cd network
     terraform init
     terraform apply -auto-approve
     cd ..
     make all
     ```
   * Observa el orden de creación y elimina (`terraform destroy`) para ver el orden de destrucción.

3. **Entrega**

   * Captura de pantalla del grafo de dependencia (`terraform graph | dot -Tpng > graph.png`).
   * Breve informe (1 página) sobre la separación unidireccional actual.

</details>

<details>
<summary><strong>Fase 2: Inyección de dependencias</strong></summary>

1. **Inversión de Control y inversión de dependencias**

   * Estudia `main.py`: allí se genera dinámicamente `main.tf.json` inyectando valores de `network`.
2. **Ejercicio práctico**

   * Modifica `main.py` para inyectar además parámetros de configuración del servidor (por ejemplo, nombre, etiquetas).
   * Vuelve a ejecutar `make all` y verifica que los nuevos parámetros aparecen en `main.tf.json`.
3. **Entrega**

   * Código modificado de `main.py`.
   * Explicación corta (máx. 300 palabras) del principio de inversión de control aplicado.

</details>

<details>
<summary><strong>Fase 3: Patrón Facade</strong></summary>

1. **Teoría**

   * ¿Cómo agruparías varios módulos (red + servidor + firewall) tras un únic "facade"?
2. **Ejercicio práctico**

   * Crea en `facade/` un `facade.tf.json` que exponga outputs simplificados (p.ej., `endpoint`, `network_id`).
   * Refactoriza `main.py` para usar este módulo de facade en lugar de llamadas directas.
3. **Entrega**

   * Código `facade/`.
   * Diagrama de alto nivel mostrando el facade.

</details>

<details>
<summary><strong>Fase 4: Patrón Adapter</strong></summary>

1. **Teoría**

   * El adaptador "envuelve" una interfaz incompatible para satisfacer otra.
2. **Ejercicio práctico**

   * Simula un módulo de "identidad" que en local usa `null_resource`, y crea un adaptador (`adapter.tf.json`) que convierta su output en formato Terraform estándar (por ejemplo, lista de usuarios -> JSON).
3. **Entrega**

   * `adapter/adapter.tf.json` y ejemplo de uso.
   * Explicación de cuándo usarías este patrón en producción.

</details>

<details>
<summary><strong>Fase 5: Patrón Mediator</strong></summary>

1. **Teoría**

   * Centraliza la coordinación entre módulos complejos.
2. **Ejercicio práctico**

   * Implementa en Python un "mediador" (`mediator.py`) que, antes de generar `main.tf.json`, consulte el estado de `network`, `server` y `firewall` y establezca triggers/dependencias.
3. **Entrega**

   * `mediator.py` con comentarios.
   * Breve comparación entre mediador y facade.

</details>

<details>
<summary><strong>Fase 6: Elección de patrón</strong></summary>

* **Actividad de discusión** (en pares o tríos):

  * Para un escenario complejo (p.ej., multi-cloud), justifica qué patrón(s) usarías y por qué.
  * Prepara una presentación de 5 min con ejemplos de código.

</details>

<details>
<summary><strong>Fase 7: Estructura y compartición de módulos</strong></summary>

1. **Monorepositorio vs multirepositorio**

   * Debate ventajas/desventajas.
2. **Ejercicio práctico**

   * Refactoriza el proyecto a multi-repositorio: extrae `network/`, `server/`, `facade/`, `adapter/`, `mediator/` a repos distintos.
   * Configura en cada uno un `README.md` y un pipeline de CI (GitHub Actions o similar).
3. **Entrega**

   * Enlaces a los repositorios creados.
   * Tabla comparativa de tiempo de desarrollo y facilidad de uso.

</details>

<details>
<summary><strong>Fase 8: Versionado y liberación</strong></summary>

1. **Versionado semántico**

   * Asigna versiones (`v1.0.0`, `v1.1.0`, etc.) a cada módulo.
2. **Ejercicio práctico**

   * Crea tags de Git y un script en `Makefile` que haga:

     ```makefile
     release:
         git tag -a v$(VERSION) -m "Release $(VERSION)"
         git push --tags
     ```
3. **Entrega**

   * `Makefile` actualizado.
   * Ejemplo de release con al menos dos versiones.

</details>

<details>
<summary><strong>Fase 9: Publicación y compartición</strong></summary>

1. **Registro local vs Terraform registry**

   * Configura `providers.tf` para usar un `registry.local` (p.ej., con `terraform local publish` o repositorio Artifactory).
2. **Ejercicio práctico**

   * Publica uno de tus módulos en un registro local y úsalo desde otro proyecto clonándolo mediante `terraform init`.
3. **Entrega**

   * Configuración de `registry` en Terraform.
   * Captura de pantalla del módulo instalado desde el registro.

</details>

#### Ejercicios adicionales

<details>
<summary>1. <strong>Explica las diferencias clave entre los patrones Facade, Adapter y Mediator en términos de acoplamiento y reutilización.</strong></summary>
</details>

<details>
<summary>2. <strong>Describe un escenario real (por ejemplo, despliegue multi-cloud) y justifica qué patrón usarías para gestionar dependencias complejas, señalando ventajas e inconvenientes de cada opción.
</strong></summary>
</details>

<details>
<summary>3. <strong>Argumenta cómo la inversión de control y la inversión de dependencias mejoran la mantenibilidad de un proyecto IaC frente a relaciones unidireccionales.
</strong></summary>


</details>

<details>
<summary>4. <strong>Analiza posibles riesgos o anti-patrones al abusar de la inyección de dependencias en módulos Terraform.
</strong></summary>

</details>

<details>
<summary>5. <strong>Compara monorepositorio vs. multirepositorio para un conjunto de módulos IaC usados por diferentes equipos. Incluye criterios de escalabilidad, gobernanza y velocidad de despliegue.
</strong></summary>

</details>

<details>
<summary>6. <strong>Diseña un flujo de trabajo de Git (ramas, tags, pull requests) adecuado para ambos modelos, destacando diferencias en la gestión de versiones compartidas.
</strong></summary>

</details>

<details>
<summary>7. <strong>Justifica el uso de versionado semántico en módulos Terraform. ¿Qué consecuencias podría tener omitirlo?</strong></summary>
</details>

<details>
<summary>8. <strong>Propón una política de gestión de releases para un registro privado de módulos, incluyendo cadencias y criterios de bump de versión (mayor, menor, parche).
</strong></summary>
</details>

<details>
<summary>9. <strong>Evalúa ventajas y desventajas de publicar módulos en Terraform Cloud Registry frente a un repositorio Git interno.
</strong></summary>
</details>

<details>
<summary>10. <strong>Describe cómo implementarías un mecanismo de autenticación y control de acceso para tu registro de módulos en un entorno corporativo.
</strong></summary>
</details>

<details>
<summary>11. <strong>Toma el módulo de red y rediseña su interfaz para que admita un nuevo recurso (por ejemplo, balanceador de carga) inyectado por un patrón Mediator. Indica qué cambios harías en la generación de la configuración y en la orquestación Python.</strong></summary>
</details>

<details>
<summary>12. <strong>Crea un módulo "unificado" que agrupe red, servidor y monitorización bajo un único facade. Describe detalladamente las entradas y salidas de ese módulo y cómo garantizarías que las dependencias internas no se expongan al consumidor.</strong></summary>
</details>

<details>
<summary>13. <strong>Diseña un adaptador que permita usar, de forma transparente, recursos de un proveedor ficticio (p. ej., "localmock") con la misma interfaz que tus módulos actuales de GCP. Explica cómo transformarías los outputs para encajar en los consumidores existentes.</strong></summary>
</details>

<details>
<summary>14. <strong>Refactoriza el proyecto original a un esquema multi-repositorio. Detalla en un documento los pasos de migración de cada módulo, la configuración de los pipelines CI/CD y los cambios en los pipelines de integración.</strong></summary>
</details>

<details>
<summary>15. <strong>Implementa en tu Makefile o en tu sistema de CI un proceso automatizado que, tras cada merge a la rama principal, actualice la versión semántica de uno de los módulos, genere un tag Git y publique el módulo en un registro local.
</strong></summary>
</details>

<details>
<summary>16. <strong>Monta un registro privado (puede ser un simple servidor HTTP o un artefacto de Git) y publica al menos dos versiones de un módulo. Luego, desde otro proyecto, configura el `source` para consumirlo por versión fija y por rango de versiones, y demuestra la actualización controlada.
</strong></summary>
</details>

#### Entregables finales

* Repositorio(s) o carpetas organizadas con código y versiones.
* Documentación (README, diagramas, tabla comparativa).
* Scripts de liberación y ejemplos de publicación.
* Informe final (3-4 páginas) que recoja:

  - Análisis de cada patrón.
  - Elecciones de diseño.
  - Comparativa mono vs multi-repositorio.
  - Práctica de versionado y publicación.
  - Ejercicios resueltos

