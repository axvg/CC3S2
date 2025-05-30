"""
counter.py
Servicio Flask que implementa un contador in-memory.
Provee rutas para crear, leer, actualizar e eliminar contadores.
"""

from flask import Flask, request
import status
from functools import wraps

app = Flask(__name__)

# Diccionario global que guarda el nombre de cada contador y su valor.
COUNTERS = {}


def require_counter(f):
    @wraps(f)
    def wrapper(name, *args, **kwargs):
        if name not in COUNTERS:
            return {"message": f"El contador '{name}' no existe"}, status.HTTP_404_NOT_FOUND
        return f(name, *args, **kwargs)
    return wrapper

@app.route("/counters/<name>", methods=["POST"])
def create_counter(name):
    """
    Crea un nuevo contador con valor inicial = 0.
    Retorna 201 (CREATED) si se crea correctamente.
    Retorna 409 (CONFLICT) si el contador ya existía.
    """
    app.logger.info(f"Solicitud para crear el contador: {name}")
    global COUNTERS

    if name in COUNTERS:
        return {"message": f"El contador '{name}' ya existe"}, status.HTTP_409_CONFLICT

    COUNTERS[name] = 0
    return {name: COUNTERS[name]}, status.HTTP_201_CREATED


@app.route("/counters/<name>", methods=["PUT"])
@require_counter
def update_counter(name):
    """
    Actualiza (p.e. incrementa) el contador <name>.
    Retorna 200 (OK) si se actualiza correctamente.
    Retorna 404 (NOT FOUND) si el contador no existe.
    """
    app.logger.info(f"Solicitud para actualizar el contador: {name}")
    COUNTERS[name] += 1
    return {name: COUNTERS[name]}, status.HTTP_200_OK


@app.route("/counters/<name>", methods=["GET"])
@require_counter
def read_counter(name):
    """
    Lee el valor actual del contador <name>.
    Retorna 200 (OK) si el contador existe.
    Retorna 404 (NOT FOUND) si el contador no existe.
    """
    app.logger.info(f"Solicitud para leer el contador: {name}")
    return {name: COUNTERS[name]}, status.HTTP_200_OK


@app.route("/counters/<name>", methods=["DELETE"])
@require_counter
def delete_counter(name):
    """
    Elimina el contador <name>.
    Retorna 204 (NO CONTENT) si la eliminación es exitosa.
    Retorna 404 (NOT FOUND) si el contador no existe.
    """
    app.logger.info(f"Solicitud para eliminar el contador: {name}")
    del COUNTERS[name]
    return "", status.HTTP_204_NO_CONTENT

def change_counter(name, delta):
    COUNTERS[name] += delta
    return {name: COUNTERS[name]}

@app.route("/counters/<name>/increment", methods=["PUT"])
@require_counter
def increment_counter(name):
    return change_counter(name, +1), status.HTTP_200_OK

@app.route("/counters/<name>/set", methods=["PUT"])
@require_counter
def set_counter(name):
    body = request.get_json()
    if body.get("value") and body.get("value") < 0:
        return {"message": f"El valor debe ser no negativo"}, status.HTTP_400_BAD_REQUEST

    COUNTERS[name] = body.get("value", COUNTERS[name])
    return {name: COUNTERS[name]}, status.HTTP_200_OK

@app.route("/counters", methods=["GET"])
def list_counters():
    return COUNTERS, status.HTTP_200_OK

@app.route("/counters/<name>/reset", methods=["PUT"])
@require_counter
def reset_counter(name):
    current_value = COUNTERS[name]
    change_counter(name, -current_value)
    return { name: COUNTERS[name] }, status.HTTP_200_OK