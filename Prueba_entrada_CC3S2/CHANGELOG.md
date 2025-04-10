# Changelog

## [v1.0-day2] - 2025-04-09
### Added
- Implementacion de la clase `Question` en `trivia.py` con:
    - Constructor (`__init__`) con validacion de parametros (descripcion, opciones, respuesta correcta).
    - Metodo `is_correct(answer)` para verificar la respuesta.
    - Metodo `__str__()` para representacion legible de la pregunta y opciones.
- Pruebas unitarias para la clase `Question` en `test_trivia.py` cubriendo:
    - Creacion valida.
    - Casos invalidos (descripcion, opciones, respuesta correcta fuera de opciones).
    - Funcionamiento de `is_correct()` (casos verdadero y falso).
    - Representacion `__str__()`.

## [v1.0-day1] - 2025-04-08
### Added
- Configuracion inicial del proyecto (venv, requirements.txt).
- Archivos `Dockerfile` y `docker-compose.yml`.
- Archivo `.gitignore`.
- Inicializacion de Git con rama `develop`.