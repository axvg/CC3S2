from fastapi.testclient import TestClient
import pytest

from main import app

client = TestClient(app)


def test_read_root_status_code():
    """Verifica que el endpoint root devuelva status 200 OK."""
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.skip(reason="TODO: make mockup for db")
def test_read_root_response_json():
    """Verifica el contenido JSON devuelto por el endpoint root."""
    response = client.get("/")
    expected_json = {"message": "API de Trivia API Default"}
    assert response.json() == expected_json


def test_get_questions():
    """Verifica que se pueden obtener todas las preguntas."""
    response = client.get("/questions")
    assert response.status_code == 200
    assert "questions" in response.json()
    assert len(response.json()["questions"]) > 0


def test_create_question():
    """Verifica que se puede crear una nueva pregunta."""
    initial_response = client.get("/questions")
    initial_count = len(initial_response.json()["questions"])

    new_question = {
        "description": "¿Cuál es la capital de Perú?",
        "options": ["Lima", "Bogotá", "Santiago", "Quito"],
        "correct_answer": "Lima",
        "difficulty": 1
    }

    response = client.post("/questions", json=new_question)
    assert response.status_code == 200

    final_response = client.get("/questions")
    final_count = len(final_response.json()["questions"])
    assert final_count == initial_count + 1
