import random
from fastapi import FastAPI
from trivia import Question, Quiz

app = FastAPI()

# --- Banco de Preguntas ---
ALL_QUESTIONS = [
    Question("Cual es la capital de Francia?",
             ["Madrid", "Londres", "Paris", "Berlin"], "Paris"),
    Question("Cual es 2 + 2?",
             ["3", "4", "5", "6"], "4"),
    Question("Planeta mas cercano al Sol?",
             ["Venus", "Marte", "Mercurio", "Tierra"], "Mercurio"),
    Question("Quien escribio 'Don Quijote de la Mancha'?",
             ["Shakespeare", "Cervantes", "Tolstoy", "Garcia Marquez"],
             "Cervantes"),
    Question("Cual es el rio mas largo del mundo?",
             ["Nilo", "Amazonas", "Misisipi", "Yangtse"], "Amazonas"),
    Question("En que anio llego el hombre a la Luna?",
             ["1965", "1969", "1971", "1975"], "1969"),
    Question("Cual es el simbolo quimico del Oro?",
             ["Ag", "O", "Au", "Fe"], "Au"),
    Question("Cuantos lados tiene un hexagono?",
             ["5", "6", "7", "8"], "6"),
    Question("Cual es el oceano mas grande?",
             ["Atlantico", "Indico", "Artico", "Pacifico"], "Pacifico"),
    Question("Quien pinto la Mona Lisa?",
             ["Miguel Angel", "Rafael", "Donatello", "Leonardo da Vinci"],
             "Leonardo da Vinci"),
    Question("Cual es la montana mas alta del mundo?",
             ["K2", "Kangchenjunga", "Makalu", "Everest"], "Everest"),
    Question("Moneda oficial de Japon?",
             ["Won", "Dolar", "Yen", "Euro"], "Yen")
]


def run_quiz(num_questions_to_ask=10):
    """Ejecuta el juego de trivia completo en la consola."""
    print("Bienvenido al juego de trivia!")
    print(f"Responde las siguientes {num_questions_to_ask} preguntas "
          "seleccionando el numero de la opcion correcta.")
    print("-" * 30)

    available_questions = len(ALL_QUESTIONS)
    if available_questions < num_questions_to_ask:
        print(f"Advertencia: No hay suficientes preguntas unicas "
              f"({available_questions}), se usaran todas.")
        questions_for_game = ALL_QUESTIONS[:]
        num_questions_to_ask = available_questions
    else:
        questions_for_game = random.sample(ALL_QUESTIONS, num_questions_to_ask)

    quiz = Quiz(total_rounds=num_questions_to_ask)
    for q in questions_for_game:
        quiz.add_question(q)

    round_number = 1
    while quiz.has_more_questions():
        question = quiz.get_next_question()
        if not question:
            break

        print(f"\nPregunta {round_number}: {question.description}")
        for idx, option in enumerate(question.options):
            print(f"{idx + 1}) {option}")

        while True:
            try:
                answer_num_str = input("Tu respuesta (numero): ")
                answer_idx = int(answer_num_str) - 1
                if 0 <= answer_idx < len(question.options):
                    chosen_option = question.options[answer_idx]
                    break
                else:
                    print(f"Numero invalido. Introduce un numero entre 1 y "
                          f"{len(question.options)}.")
            except ValueError:
                print("Entrada invalida. Por favor, introduce un numero.")

        is_correct = quiz.answer_question(question, chosen_option)
        if is_correct:
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta era: "
                  f"{question.correct_answer}")

        round_number += 1
        print("-" * 10)

    print("\n" + "=" * 30)
    print("Juego terminado. Aqui esta tu puntuacion:")
    score = quiz.get_score()
    print(f"Preguntas contestadas: {score['answered']}")
    print(f"Respuestas correctas: {score['correct']}")
    print(f"Respuestas incorrectas: {score['incorrect']}")
    print("=" * 30)


if __name__ == "__main__":
    run_quiz(num_questions_to_ask=10)


@app.get("/")
def read_root():
    """Endpoint raiz de la API."""
    return {"message": "API de Trivia"}
