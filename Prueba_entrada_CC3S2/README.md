# Prueba_entrada_CC3S2

## Proyecto: Juego de Trivia con FastAPI, PostgreSQL

Este proyecto implementa un juego de trivia con API REST usando FastAPI y PostgreSQL database. Incluye pruebas unitarias con pytest, lint con flake8 integracion, pipeline CI/CD con github actions, analisis de seguridad con Bandit y prueba de carga con locust.

---

## Para probar el proyecto en local

### 1. Clona el repositorio

```sh
git clone https://github.com/axvg/CC3S2.git
cd Prueba_entrada_CC3S2/trivia_game_python
```

### 2. Copia el archivo de variables de enterno

```sh
cp .env.example .env
```

### 3. Levanta la base de datos y API con Docker Compose

```sh
make up # si se tiene GNU Make
```

Si no se tiene  GNU Make
```sh
docker-compose up --build
```

Esto levantara:
- PostgreSQL db en el puerto 5432
- FastAPI api en el puerto 8000

### 4. Accede a la API

- Documentacion interactiva: [http://localhost:8000/docs](http://localhost:8000/docs)
- Endpoint de `questions`: [http://localhost:8000/questions]

- Al inicio no habra preguntas porque la base de datos sera nueva, para crear preguntas se puede usar la documentacion interactiva usando `POST` requests.