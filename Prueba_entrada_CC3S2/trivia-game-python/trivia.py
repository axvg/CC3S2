class Question:
    def __init__(self, description, options, correct_answer):
        if not isinstance(description, str) or not description:
            raise ValueError("La descripcion no puede estar vacia.")
        if not isinstance(options, list) or len(options) < 2:
             raise ValueError("Debe haber al menos dos opciones.")
        if correct_answer not in options:
            raise ValueError("La respuesta correcta debe estar entre las opciones.")

        self.description = description
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        return self.correct_answer == answer

    def __str__(self):
        options_str = "\n".join(f"{i+1}) {opt}" for i, opt in enumerate(self.options))
        return f"{self.description}\n{options_str}"

class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0

    def add_question(self, question):
        if not isinstance(question, Question):
            raise TypeError("Solo se pueden anadir objetos de tipo Question.")
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    def has_more_questions(self):
        """Verifica si quedan preguntas por responder."""
        return self.current_question_index < len(self.questions)