# import random

class Question:
    """Clase usada para preguntas de trivia con
        opciones y respuesta correcta."""

    def __init__(self, description, options, correct_answer):
        """
        Inicializa una pregunta.

        Args:
            description (str): El texto de la pregunta.
            options (list): Una lista de posibles respuestas str[].
            correct_answer (str): La respuesta correcta.
        """
        if not isinstance(description, str) or not description:
            raise ValueError("La descripcion no puede estar vacia.")
        if not isinstance(options, list) or len(options) < 2:
            raise ValueError("Debe haber al menos dos opciones.")
        if correct_answer not in options:
            raise ValueError(
                "La respuesta correcta debe estar entre las opciones."
            )

        self.description = description
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        """
        Verifica si la respuesta proporcionada es la correcta.

        Args:
            answer (str): La respuesta seleccionada por el jugador.

        Returns:
            bool: True si la respuesta es correcta, False en caso contrario.
        """
        return self.correct_answer == answer

    def __str__(self):
        """Representacion en string de la pregunta y sus opciones."""
        options_str = "\n".join(
            f"{i + 1}) {opt}" for i, opt in enumerate(self.options)
        )
        return f"{self.description}\n{options_str}"


class Quiz:
    """Maneja el flujo del juego de trivia,
        incluyendo preguntas y puntuacion."""

    def __init__(self, total_rounds=10):
        """Inicializa un nuevo juego de trivia."""
        self.questions = []
        self.current_question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.total_rounds = total_rounds

    def add_question(self, question):
        """Agrega una pregunta al quiz."""
        if not isinstance(question, Question):
            raise TypeError("Solo se pueden agregar objetos de tipo Question.")
        self.questions.append(question)

    def get_next_question(self):
        """
        Obtiene la siguiente pregunta si no se ha alcanzado el limite de rondas
        y si quedan preguntas disponibles.
        """
        rounds_limit = self.current_question_index >= self.total_rounds
        questions_limit = self.current_question_index >= len(self.questions)
        if rounds_limit or questions_limit:
            return None

        question = self.questions[self.current_question_index]
        self.current_question_index += 1    # avanzamos
        return question

    def answer_question(self, question, answer):
        """
        Procesa la respuesta del jugador, actualiza puntuacion.

        Args:
            question (Question): La pregunta que se respondio.
            answer (str): La respuesta seleccionada por el jugador.

        Returns:
            bool: True si la respuesta es correcta, False en caso contrario.
        """
        if not isinstance(question, Question):
            raise TypeError(
                "El primer argumento debe ser una instancia de Question."
                )

        is_correct = question.is_correct(answer)
        if is_correct:
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1
        return is_correct

    def has_more_questions(self):
        """
        Verifica si el juego debe continuar.
        """
        # Linea potencialmente larga, verificar y dividir si es necesario
        within_rounds = self.current_question_index < self.total_rounds
        within_questions = self.current_question_index < len(self.questions)
        return within_rounds and within_questions

    def get_score(self):
        """Devuelve la puntuacion actual"""
        total_answered = self.correct_answers + self.incorrect_answers
        return {
            "answered": total_answered,
            "correct": self.correct_answers,
            "incorrect": self.incorrect_answers,
        }
