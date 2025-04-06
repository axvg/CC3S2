   #  Informe sobre la importancia de IaC, contenedores, K8s, observabilidad y CI/CD:

Estas tecnologias son la base para entregar software agil y confiable hoy en dia. IaC (Infraestructura como Codigo) da consistencia y velocidad al crear entornos, todo versionado en Git. Contenedores (Docker) empaquetan la aplicacion y sus dependencias, asegurando que corra igual en cualquier lado. Kubernetes (K8s) orquesta esos contenedores a escala, manejando despliegues, escalado y recuperacion automaticamente. CI/CD automatiza todo el ciclo desde el commit hasta el despliegue, eliminando trabajo manual y errores. Finalmente, la Observabilidad (Prometheus, Grafana) te permite entender que pasa en produccion, detectar problemas rapido y mejorar continuamente. En combinacion, permiten ciclos de entrega muy cortos, alta disponibilidad y capacidad de respuesta al negocio.

## Identificar riesgos y desafios:

Sobrecarga Cognitiva: Los desarrolladores pueden sentirse abrumados y que son muchas herramientas y conceptos nuevos que el equipo debe aprender (IaC, Docker, K8s, PromQL, CI/CD). si tienen que manejar demasiada complejidad de la infraestructura ademas de la aplicacion aca puede ayudar la Ingenieria de Plataformas.

Configuración de seguridad: Automatizar la infraestructura y los despliegues introduce nuevos riesgos de ataque si no se configuran bien los permisos, secretos y escaneos de seguridad en el pipeline.

La facilidad para crear recursos puede llevar a gastos inesperados si no hay buen control y monitoreo de costos.