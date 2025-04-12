# Changelog

## [Unreleased]

## [v1.0-day4] - 2025-04-11
### Added
- Sistema de puntuacion en clase `Quiz`:
    - Atributos `correct_answers` e `incorrect_answers`.
    - Metodo `answer_question(question, answer)` para procesar respuesta y actualizar puntuacion.
    - Metodo `get_score()` para obtener resumen de puntuacion.
- Logica de rondas en clase `Quiz`:
    - Atributo `total_rounds` (configurable, por defecto 10).
    - `get_next_question()` y `has_more_questions()` ahora respetan `total_rounds`.
- Implementacion del flujo de juego en `main.py` (`run_quiz`):
    - Bienvenida e instrucciones.
    - Seleccion y mezcla de N preguntas de un banco (`ALL_QUESTIONS`).
    - Bucle principal para N rondas: muestra pregunta, obtiene input del usuario (con validacion basica), procesa respuesta y da feedback.
    - Muestra resumen final de puntuacion.
- Preguntas de ejemplo (`ALL_QUESTIONS`) en `main.py`.
- Pruebas unitarias en `test_trivia.py` para:
    - Puntuacion inicial.
    - Logica de `answer_question` (correcta/incorrecta).
    - Puntuacion acumulada.
    - Limite de rondas (`total_rounds`).
- `flake8` añadido, fix de archivos *.py para flake8.


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