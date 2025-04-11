import pytest
from trivia import Question, Quiz

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

Q1 = Question("Pregunta 1", ["A", "B"], "A")
Q2 = Question("Pregunta 2", ["C", "D", "E"], "D")

def test_quiz_creation():
    quiz = Quiz()
    assert isinstance(quiz.questions, list)
    assert len(quiz.questions) == 0
    assert quiz.current_question_index == 0
    assert quiz.has_more_questions() is False

def test_quiz_add_question_valid():
    quiz = Quiz()
    quiz.add_question(Q1)
    assert len(quiz.questions) == 1
    assert quiz.questions[0] == Q1
    assert quiz.has_more_questions() is True
    quiz.add_question(Q2)
    assert len(quiz.questions) == 2
    assert quiz.questions[1] == Q2

def test_quiz_add_question_invalid_type():
    quiz = Quiz()
    with pytest.raises(TypeError, match="Solo se pueden anadir objetos de tipo Question"):
        quiz.add_question("esto no es valido")
    with pytest.raises(TypeError):
        quiz.add_question(123)

def test_quiz_get_next_question_flow():
    quiz = Quiz()
    quiz.add_question(Q1)
    quiz.add_question(Q2)

    assert quiz.current_question_index == 0
    assert quiz.has_more_questions() is True
    next_q = quiz.get_next_question()
    assert next_q == Q1
    assert quiz.current_question_index == 1

    assert quiz.has_more_questions() is True
    next_q = quiz.get_next_question()
    assert next_q == Q2
    assert quiz.current_question_index == 2

    assert quiz.has_more_questions() is False
    next_q = quiz.get_next_question()
    assert next_q is None
    assert quiz.current_question_index == 2

    next_q = quiz.get_next_question()
    assert next_q is None
    assert quiz.current_question_index == 2

def test_quiz_get_next_question_when_empty():
     quiz = Quiz()
     assert quiz.has_more_questions() is False
     assert quiz.get_next_question() is None
     assert quiz.current_question_index == 0

def test_quiz_has_more_questions():
    quiz = Quiz()
    assert quiz.has_more_questions() is False
    quiz.add_question(Q1)
    assert quiz.has_more_questions() is True
    quiz.get_next_question()
    assert quiz.has_more_questions() is False