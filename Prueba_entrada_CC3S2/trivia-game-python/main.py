from fastapi import FastAPI
from trivia import Question, Quiz

app = FastAPI()

def run_basic_quiz():
    print("Iniciando...")

    q1 = Question("Cual es la capital de Francia?", ["Madrid", "Londres", "Paris", "Berlin"], "Paris")
    q2 = Question("Cual es 2 + 2?", ["3", "4", "5", "6"], "4")
    q3 = Question("Planeta mas cercano al Sol?", ["Venus", "Marte", "Mercurio", "Tierra"], "Mercurio")

    quiz = Quiz()
    try:
        quiz.add_question(q1)
        quiz.add_question(q2)
        quiz.add_question(q3)
    except TypeError as e:
         print(f"Error anadiendo pregunta: {e}")


    print("\nAqui estan las preguntas:")
    question_number = 1
    while quiz.has_more_questions():
         current_question = quiz.get_next_question()
         if current_question:
             print(f"\n--- Pregunta {question_number} ---")
             print(current_question)
             question_number += 1

    print("\n--- Fin del Quiz Basico (No hay mas preguntas) ---")

if __name__ == "__main__":
    run_basic_quiz()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Trivia (en desarrollo)"}