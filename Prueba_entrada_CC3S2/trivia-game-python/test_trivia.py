import pytest
from trivia import Question

# data to test
QUESTION_DESC = "¿Cual es la capital de Francia?"
OPTIONS = ["Madrid", "Londres", "Paris", "Berlin"]
CORRECT_ANSWER = "Paris"
INCORRECT_ANSWER = "Londres"

def test_question_creation_valid():
    """Verifica que una pregunta se crea correctamente con datos validos."""
    q = Question(QUESTION_DESC, OPTIONS, CORRECT_ANSWER)
    assert q.description == QUESTION_DESC
    assert q.options == OPTIONS
    assert q.correct_answer == CORRECT_ANSWER

def test_question_creation_invalid_description():
    """Verifica que falla si la descripcion es invalida."""
    with pytest.raises(ValueError):
        Question("", OPTIONS, CORRECT_ANSWER)
    with pytest.raises(ValueError):
         Question(None, OPTIONS, CORRECT_ANSWER)

def test_question_creation_invalid_options():
    """Verifica que falla si las opciones son invalidas."""
    with pytest.raises(ValueError):
        Question(QUESTION_DESC, ["Solo una"], "Solo una") # Menos de 2 opciones
    with pytest.raises(ValueError):
         Question(QUESTION_DESC, "no es lista", "opcion")

def test_question_creation_correct_answer_not_in_options():
    """Verifica que falla si la respuesta correcta no esta en las opciones."""
    with pytest.raises(ValueError):
        Question(QUESTION_DESC, OPTIONS, "Roma")

def test_is_correct_true():
    """Verifica que is_correct devuelve True para la respuesta correcta."""
    q = Question(QUESTION_DESC, OPTIONS, CORRECT_ANSWER)
    assert q.is_correct(CORRECT_ANSWER) is True

def test_is_correct_false():
    """Verifica que is_correct devuelve False para una respuesta incorrecta."""
    q = Question(QUESTION_DESC, OPTIONS, CORRECT_ANSWER)
    assert q.is_correct(INCORRECT_ANSWER) is False

def test_question_str_representation():
    """Verifica la representación en string de la pregunta."""
    q = Question(QUESTION_DESC, OPTIONS, CORRECT_ANSWER)
    expected_str = (
        "¿Cual es la capital de Francia?\n"
        "1) Madrid\n"
        "2) Londres\n"
        "3) Paris\n"
        "4) Berlin"
    )
    assert str(q) == expected_str