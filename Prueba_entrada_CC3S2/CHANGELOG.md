# Changelog

## [v1.0-day7] - 2025-04-15
### Added
- Integración completa de FastAPI con PostgreSQL usando SQLAlchemy.
- Endpoints `/questions` (GET y POST) ahora usan la base de datos.
- Uso de variables de entorno y archivo `.env.example` para configuración de la base de datos. Este debe cambiarse de nombre a `.env` para la prueba local.
- Decorador `@pytest.mark.skip` para saltar tests de API si es necesario.
- Pipeline de GitHub Actions ejecuta tests, lint, bandit y pruebas de carga con Locust.

### Changed
- Docker Compose actualizado para levantar tanto la API como PostgreSQL.
- Refactorización de la lógica de preguntas para usar SQLAlchemy en vez de listas en memoria.

### Fixed
- Corrección de variables de entorno inconsistentes entre `.env`, `docker-compose.yml` y el código.
- Solución de problemas de importación y dependencias en los tests de integración.


##  [v1.0-day6] - 2025-04-13
### Added
- Archivo de workflow de GitHub Actions `.github/workflows/pe.yml`:
    - Se ejecuta en push/pull_request `develop`.
    - Ejecuta `flake8` para linting.
    - Ejecuta `bandit` para analisis de seguridad basico.
    - Ejecuta `pytest` para correr todas las pruebas (unitarias y de integracion).
- Pruebas de integracion basicas en `test_api.py`:

## [v1.0-day5] - 2025-04-12
### Added
- Atributo `difficulty` a la clase `Question` (con tests).
- Banco de preguntas `ALL_QUESTIONS` actualizado con niveles de dificultad.
- Resumen detallado de errores al final del juego en `run_quiz`.
- `flake8-html` para reportes diarios en html.
### Changed
- `run_quiz` modificado para integrar seleccion por dificultad.
- Update de pruebas unitarias para dificultad.
- Interfaz de usuario en consola (`run_quiz`) mejorada (clear_console, emojis).

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