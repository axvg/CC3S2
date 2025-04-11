# Changelog

## [Unreleased]

## [v1.0-day3] - 2025-04-10
### Added
- Implementacion de la clase `Quiz` en `trivia.py`:
    - Constructor (`__init__`).
    - Metodo `add_question(question)` con validacion de tipo.
    - Metodo `get_next_question()` para obtener la siguiente pregunta o None.
    - Metodo `has_more_questions()` para verificar si quedan preguntas.
- Funcion `run_basic_quiz()` en `main.py` para demostracion basica en temrinal.
- Pruebas unitarias para la clase `Quiz` en `test_trivia.py` que cubren:
    - Creacion.
    - Adicion de preguntas (validas e invalidas).
    - Flujo de `get_next_question()` y `has_more_questions()`.

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