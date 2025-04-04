## Actividad: Introducción a DevOps

### Parte 1

- **¿Qué es DevOps?**

Devops es metodologia integral que busca unir equipos de desarrollo, QA y operaciones. El proceso debe ser colaborativo y continuo. No solo son herramientas o individuos.

- **Historia y antecedentes de DevOps.**

Devops surgio como una respuesta a limitaciones de modelos tradicionales de desarrollo donde los equipos estaban aislados y con largos ciclos de actualizacion


- **Diferencias entre los equipos de desarrollo y operaciones en el pasado.**

El modelo de equipo pasado tenia los roles definidos y separados: Dev y Ops con muros conceptuales.

Esta divisiones generaba silos y muros conceptuales asi como ciclos de retroalimentación prolongados


- **Principios fundamentales de DevOps** (enfoque en el cliente, equipos autónomos y multifuncionales, mejora continua, automatización).

Los principios clave incluyen:

* Cultura de colaboracion y responsabilidad Compartida: Romper silos y fomentar la comunicacion de esta manera todos son responsables del proceso.

* Automatizacion: Automatizar tareas repetitivas y que pueden ocasionar errores en el proceso. La Integracion Continua (CI) y la Entrega/Despliegue Continuo (CD) son usadas para esto.

* Equipos autonomos y multifuncionales: Equipos pequeños que poseen todas las habilidades necesarias (Dev, QA, Ops, Sec) para diseñar, construir, probar, desplegar y operar en el proceso.

* Monitoreo y Observabilidad: Medir y entender el comportamiento del sistema en producción para detectar problemas, tomar decisiones informadas y dar informacion a la mejora continua.


- **Qué NO es DevOps.**

DevOps no son herraminetos, no es un producto, no es una especificacion o un titulo. No es una solucion magica.



#### 2. Preguntas de reflexión  

1. **¿Por qué surgió la necesidad de DevOps en el desarrollo de software?**

Esta necesidad surgio debido a la ineficiencia del modelo tradicional que separaba las responsabilidades y generaba "silos" (equipos aislado). Este modelo funcionaba debido a que el software anteriormente requeria menos actualizaciones.


2. **Explica cómo la falta de comunicación y coordinación entre los equipos de desarrollo y operaciones en el pasado llevó a la creación de DevOps.**

Debido a que cada grupo se especializaba en una fase del proceso, se generaban muros conceptuales, esto conllevaba a que si ocurria un problema se pudiera echar la culpa entre equipos. Este enfoque previo requeria una vision mas integral de las responsabilidades cubriendo asi desde el inicio hasta el fin del proceso.


3. **Describe cómo el principio de mejora continua impacta tanto en los aspectos técnicos como en los culturales de una organización.**

La mejora continua  impacta en:

El Impacto Tecnico:

Eficiencia operativa: Debido a la mejora eficiencias en pipelines.

Adopcion de nuevas tecnologias: La mejora tambien influye en la investigacion de nuevas herramientas que se pueden utilizar en el proceso, como cambio de servicios en la nube, mejoras de seguridad.

Impacto Cultural:

Aprendizaje constante: El enfoque integral permite compartir conocimientos e impulsa la curiosidad.

Mejor de ambiente laboral: Crear un ambiente donde sea seguro señalar problemas, proponer mejoras o admitir errores sin temor a represalias


4. **¿Qué significa que DevOps no se trata solo de herramientas, individuos o procesos?** 

Significa que DevOps es una metodologia integral que involucra a las herramientas, individups y procesos junto a un cambio cultural en los equipos que mejora la comunicacion.


5. **Según el texto, ¿cómo contribuyen los equipos autónomos y multifuncionales a una implementación exitosa de DevOps?**  

Este tipo de equipos rompen los silos organizacionales que se tenian en equipos tradicionales. Esto se hace debido a que se tienen las responsabilidades y conocimientos de manera compartida.


### Parte 2

1. **¿Qué significa "desplazar a la izquierda" en el contexto de DevSecOps y por qué es importante?**

Se trata de meter las practicas y herramientas de seguridad lo mas temprano posible en el ciclo de vida del desarrollo. Es decir, en vez de esperar al final, justo antes de salir a produccion (que seria la derecha del ciclo), pones la seguridad desde el diseño, la codificacion, las pruebas, en cada fase "izquierda".

Esta es importante porque cuando se esta escribiendo el codigo es mucho mas "barato" y facil de arreglar que si lo encuentras ya en produccion.


2. **Explica cómo IaC mejora la consistencia y escalabilidad en la gestión de infraestructuras.**  

Debido a que cambia las reglas del juego de la siguiente manera:

Consistencia: Al definir servidores, redes, bases de datos en archivos de texto y con herramientas (como Terraform o Ansible), te aseguras de que cada vez que despliegas, el entorno es exactamente igual.

Escalabilidad: Si se necesitan mas maquinas se cambia el numero en el texto (count = 10 en vez de count = 3) y ejecutas el comando con la herramienta.


3. **¿Cuál es la diferencia entre monitoreo y observabilidad? ¿Por qué es crucial la observabilidad en sistemas complejos?**  

La diferencia radica en que el monitoreo se basa en metricas (cantidades) y la observabilidad usa metricas, logs (registro de eventos) y trazas (seguimiento).


4. **¿Cómo puede la experiencia del desarrollador impactar el éxito de DevOps en una organización?**  

Esta experiencia es la comodidad que tiene el desarrollador para realizar su labor. Si se tienen pipelines lentas, mala documentacion, la experiencia sera mala y el desarrollar podria no aplicar las buenas practicas y entregar software de baja calidad.


5. **Describe cómo InnerSource puede ayudar a reducir silos dentro de una organización.**  

InnerSource es  aplicar las ideas del mundo open source (codigo abierto) pero dentro de la empresa. Esto es, compartir codigo entre equipos, permitir que otros equipos contribuyan a tu codigo (con revisiones) y reutilizar componentes .


6. **¿Qué rol juega la ingeniería de plataformas en mejorar la eficiencia y la experiencia del desarrollador?** 

La ingenieria de plataformas consiste en crear y mantener plataformas internas para los equipos de desarrollo. Esta plataforma ofrece un conjunto de herramientas y servicios ya listos y faciles de usar para construir, desplegar y operar aplicaciones. Esto genera mejoras en la experiencia del desarrollador y en la eficiencia.