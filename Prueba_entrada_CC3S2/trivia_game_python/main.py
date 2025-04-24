import random
import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from dotenv import load_dotenv
from typing import Optional, List
from trivia import Question, Quiz

load_dotenv()

database_url = os.getenv("DATABASE_URL")
app_title = os.getenv("APP_TITLE", "Trivia API Default")

app = FastAPI(title=app_title)


engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class QuestionDB(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    options = Column(ARRAY(String), nullable=False)
    correct_answer = Column(String, nullable=False)
    difficulty = Column(Integer, default=1)


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


ALL_QUESTIONS = [
    # Facil
    Question("Cual es 2 + 2?", ["3", "4", "5", "6"], "4", difficulty=1),
    Question(
        "Cuantos lados tiene un hexagono?", ["5", "6", "7", "8"], "6", difficulty=1
    ),
    Question(
        "Cual es la capital de Francia?",
        ["Madrid", "Londres", "Paris", "Berlin"],
        "Paris",
        difficulty=1,
    ),
    Question(
        "Cual es el simbolo quimico del Oro?",
        ["Ag", "O", "Au", "Fe"],
        "Au",
        difficulty=1,
    ),
    # Media
    Question(
        "Quien pinto la Mona Lisa?",
        ["Miguel Angel", "Rafael", "Donatello", "Leonardo da Vinci"],
        "Leonardo da Vinci",
        difficulty=2,
    ),
    Question(
        "Planeta mas cercano al Sol?",
        ["Venus", "Marte", "Mercurio", "Tierra"],
        "Mercurio",
        difficulty=2,
    ),
    Question(
        "Moneda oficial de Japon?", ["Won", "Dolar", "Yen", "Euro"], "Yen", difficulty=2
    ),
    Question(
        "En que anio llego el hombre a la Luna?",
        ["1965", "1969", "1971", "1975"],
        "1969",
        difficulty=2,
    ),
    # Dificil
    Question(
        "Quien escribio 'Don Quijote de la Mancha'?",
        ["Shakespeare", "Cervantes", "Tolstoy", "Garcia Marquez"],
        "Cervantes",
        difficulty=3,
    ),
    Question(
        "Cual es el rio mas largo del mundo?",
        ["Nilo", "Amazonas", "Misisipi", "Yangtse"],
        "Amazonas",
        difficulty=3,
    ),
    Question(
        "Cual es el oceano mas grande?",
        ["Atlantico", "Indico", "Artico", "Pacifico"],
        "Pacifico",
        difficulty=3,
    ),
    Question(
        "Cual es la montana mas alta del mundo?",
        ["K2", "Kangchenjunga", "Makalu", "Everest"],
        "Everest",
        difficulty=3,
    ),
]


def clear_console():
    """Limpia la consola en Windows o Linux/Mac de forma segura."""
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except Exception:
        pass


def run_quiz(num_questions_to_ask=10):
    """Ejecuta el juego de trivia completo."""
    print("Bienvenido al juego de trivia!")
    print(
        "Responde las siguientes preguntas seleccionando el numero de "
        "la opcion correcta."
    )
    print("La dificultad se ajustara segun tu desempeno.")
    print("-" * 50)

    quiz = Quiz(total_rounds=num_questions_to_ask)
    performance = 0.5  # Valor inicial
    current_difficulty = 1  # Dificultad inicial
    available_questions = ALL_QUESTIONS.copy()

    while quiz.has_more_questions() and available_questions:
        total_answered = quiz.correct_answers + quiz.incorrect_answers

        if total_answered > 0:
            performance = quiz.correct_answers / total_answered

        if performance >= 0.7:
            current_difficulty = 3
        elif performance >= 0.4:
            current_difficulty = 2
        else:
            current_difficulty = 1

        matching_questions = [
            q for q in available_questions if q.difficulty == current_difficulty
        ]

        # Si no hay preguntas de current_difficulty, usa las disponibles
        if not matching_questions:
            matching_questions = available_questions

        if matching_questions:
            current_question = random.choice(matching_questions)
            available_questions.remove(current_question)  # Evita repeticion

            quiz.add_question(current_question)
            question = quiz.get_next_question()

            print(
                f"\n--- Pregunta {quiz.current_question_index} "
                f"(Dificultad: {question.difficulty}/3) ---"
            )
            print(question.description)

            for i, option in enumerate(question.options, 1):
                print(f"{i}) {option}")

            try:
                user_input = input("\nSelecciona tu respuesta (numero): ")
                user_choice = int(user_input)
                if 1 <= user_choice <= len(question.options):
                    selected_answer = question.options[user_choice - 1]

                    result = quiz.answer_question(question, selected_answer)

                    if result:
                        print("Correcto! ✅")
                    else:
                        print(
                            "Incorrecto ❌. La respuesta correcta era: "
                            f"{question.correct_answer}"
                        )
                        quiz.incorrect_answers += 1
                    print("\nPresiona Enter para continuar...")
                    input()
                    clear_console()
            except ValueError:
                print("Entrada invalida. Se considera como respuesta incorrecta.")
                quiz.incorrect_answers += 1
        else:
            print("No hay mas preguntas disponibles.")
            break

    print("\n" + "=" * 50)
    print("Juego terminado. Aqui esta tu puntuacion:")
    print(f"Preguntas contestadas: {quiz.current_question_index}")
    print(f"Respuestas correctas: {quiz.correct_answers}")
    print(f"Respuestas incorrectas: {quiz.incorrect_answers}")

    print("=" * 50)


class QuestionModel(BaseModel):
    description: Optional[str] = ""
    options: List[str] = []
    correct_answer: Optional[str] = ""
    difficulty: int = 1

    class Config:
        from_attributes = True


@app.get("/")
async def root():
    return {"message": f"API de {app.title}"}


@app.get("/questions")
async def get_questions(db: Session = Depends(get_db)):
    questions = db.query(QuestionDB).all()
    return {"questions": [QuestionModel.from_orm(q) for q in questions]}


@app.post("/questions")
async def create_question(q: QuestionModel, db: Session = Depends(get_db)):
    if q.correct_answer not in q.options:
        raise HTTPException(
            status_code=400,
            detail="La respuesta correcta debe estar entre las opciones.",
        )
    question = QuestionDB(
        description=q.description,
        options=q.options,
        correct_answer=q.correct_answer,
        difficulty=q.difficulty,
    )
    db.add(question)
    db.commit()
    db.refresh(question)
    return {"message": "Pregunta agregada exitosamente.", "id": question.id}


if __name__ == "__main__":
    run_quiz(num_questions_to_ask=10)
