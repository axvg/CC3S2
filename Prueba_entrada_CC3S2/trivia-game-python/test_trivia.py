import pytest
from trivia import Question, Quiz

QUESTION_DESC = "¿Cual es la capital de Francia?"
OPTIONS = ["Madrid", "Londres", "Paris", "Berlin"]
CORRECT_ANSWER = "Paris"
INCORRECT_ANSWER = "Londres"


# --- Pruebas para Question ---
def test_question_creation_valid():
    """Verifica que una pregunta se crea correctamente con datos validos."""
    q = Question(QUESTION_DESC, OPTIONS, CORRECT_ANSWER)
    assert q.description == QUESTION_DESC
    assert q.options == OPTIONS
    assert q.correct_answer == CORRECT_ANSWER
    assert q.difficulty == 1


def test_question_creation_invalid_description():
    """Verifica que falla si la descripcion es invalida."""
    with pytest.raises(ValueError):
        Question("", OPTIONS, CORRECT_ANSWER)
    with pytest.raises(ValueError):
        Question(None, OPTIONS, CORRECT_ANSWER)


def test_question_creation_invalid_options():
    """Verifica que falla si las opciones son invalidas."""
    with pytest.raises(ValueError):
        Question(QUESTION_DESC, ["Solo una"], "Solo una")
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
    """Verifica la representacion en string de la pregunta."""
    q = Question(QUESTION_DESC, OPTIONS, CORRECT_ANSWER)
    # Dividir string largo para cumplir E501
    expected_str = (
        "[Dificultad 1]\n"
        "¿Cual es la capital de Francia?\n"
        "1) Madrid\n"
        "2) Londres\n"
        "3) Paris\n"
        "4) Berlin"
    )
    assert str(q) == expected_str


def test_question_creation_with_difficulty():
    """Verifica creacion con dificultad especifica."""
    q = Question("Desc", ["A", "B"], "A", difficulty=2)
    assert q.difficulty == 2


def test_question_creation_invalid_difficulty():
    """Verifica que falla con dificultad invalida."""
    with pytest.raises(ValueError):
        Question("Desc", ["A", "B"], "A", difficulty=0)
    with pytest.raises(ValueError):
        Question("Desc", ["A", "B"], "A", difficulty=-1)
    with pytest.raises(ValueError):
        Question("Desc", ["A", "B"], "A", difficulty=1.5)


# --- Pruebas para la clase Quiz ---

Q1 = Question("Pregunta 1", ["A", "B"], "A")
Q2 = Question("Pregunta 2", ["C", "D", "E"], "D")
Q3 = Question("Pregunta 3", ["F", "G"], "G")


def test_quiz_creation():
    """Verifica que un Quiz se crea vacio correctamente."""
    quiz = Quiz()
    assert isinstance(quiz.questions, list)
    assert len(quiz.questions) == 0
    assert quiz.current_question_index == 0
    assert quiz.has_more_questions() is False


def test_quiz_add_question_valid():
    """Verifica que se anaden preguntas Question validas."""
    quiz = Quiz()
    quiz.add_question(Q1)
    assert len(quiz.questions) == 1
    assert quiz.questions[0] == Q1
    assert quiz.has_more_questions() is True
    quiz.add_question(Q2)
    assert len(quiz.questions) == 2
    assert quiz.questions[1] == Q2


def test_quiz_add_question_invalid_type():
    """Verifica que falla al anadir algo que no es Question."""
    quiz = Quiz()
    # Corregir el mensaje esperado para que coincida con el error real
    msg = r"Solo se pueden agregar objetos de tipo Question\."
    with pytest.raises(TypeError, match=msg):
        quiz.add_question("esto no es valido")
    with pytest.raises(TypeError):
        quiz.add_question(123)


def test_quiz_get_next_question_flow():
    """Verifica el flujo completo de obtener preguntas."""
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
    """Verifica que get_next_question devuelve None si el quiz esta vacio."""
    quiz = Quiz()
    assert quiz.has_more_questions() is False
    assert quiz.get_next_question() is None
    assert quiz.current_question_index == 0


def test_quiz_has_more_questions():
    """Verifica el estado de has_more_questions."""
    quiz = Quiz()
    assert quiz.has_more_questions() is False
    quiz.add_question(Q1)
    assert quiz.has_more_questions() is True
    quiz.get_next_question()
    assert quiz.has_more_questions() is False


# --- Pruebas para Puntuacion en Quiz ---

def test_quiz_initial_score():
    """Verifica que la puntuacion inicial es cero."""
    quiz = Quiz()
    score = quiz.get_score()
    assert score["answered"] == 0
    assert score["correct"] == 0
    assert score["incorrect"] == 0
    assert quiz.correct_answers == 0
    assert quiz.incorrect_answers == 0


def test_quiz_answer_question_correct():
    """Verifica que responder correctamente incrementa el puntaje correcto."""
    quiz = Quiz()
    q = Question("Pregunta Test", ["Opcion A", "Opcion B"], "Opcion B")
    quiz.add_question(q)

    result = quiz.answer_question(q, "Opcion B")
    assert result is True
    assert quiz.correct_answers == 1
    assert quiz.incorrect_answers == 0
    score = quiz.get_score()
    assert score["answered"] == 1
    assert score["correct"] == 1
    assert score["incorrect"] == 0


def test_quiz_answer_question_incorrect():
    """Verifica que responder incorrectamente
        incrementa el puntaje incorrecto."""
    quiz = Quiz()
    q = Question("Pregunta Test", ["Opcion A", "Opcion B"], "Opcion B")
    quiz.add_question(q)

    result = quiz.answer_question(q, "Opcion A")
    assert result is False
    assert quiz.correct_answers == 0
    assert quiz.incorrect_answers == 1
    score = quiz.get_score()
    assert score["answered"] == 1
    assert score["correct"] == 0
    assert score["incorrect"] == 1


def test_quiz_multiple_answers():
    """Verifica la puntuacion despues de varias respuestas."""
    quiz = Quiz()
    quiz.add_question(Q1)
    quiz.add_question(Q2)
    quiz.add_question(Q3)

    quiz.answer_question(Q1, "A")
    quiz.answer_question(Q2, "C")
    quiz.answer_question(Q3, "F")

    assert quiz.correct_answers == 1
    assert quiz.incorrect_answers == 2
    score = quiz.get_score()
    assert score["answered"] == 3
    assert score["correct"] == 1
    assert score["incorrect"] == 2


def test_quiz_answer_question_invalid_arg():
    """Verifica que answer_question falla si no se le pasa una Question."""
    quiz = Quiz()
    with pytest.raises(TypeError):
        quiz.answer_question("no soy pregunta", "respuesta")


def test_quiz_stops_after_total_rounds():
    """Verifica que has_more_questions y
        get_next_question respetan total_rounds."""
    quiz = Quiz(total_rounds=2)
    quiz.add_question(Q1)
    quiz.add_question(Q2)
    quiz.add_question(Q3)

    assert quiz.has_more_questions() is True
    assert quiz.get_next_question() == Q1
    assert quiz.current_question_index == 1

    assert quiz.has_more_questions() is True
    assert quiz.get_next_question() == Q2
    assert quiz.current_question_index == 2

    assert quiz.has_more_questions() is False
    assert quiz.get_next_question() is None
    assert quiz.current_question_index == 2
