from fastapi import FastAPI, Depends, HTTPException
from schemas.schemas import FlashCardCreate, FlashCardResponse, Materials, Subject
from sqlalchemy.orm import Session
from db.database import SessionLocal, engine, Base
from models.models import FlashCard

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.get("/")
# def read_root(db: Session = Depends(get_db)):
#     # Example query using SQLAlchemy
#     result = db.execute("SELECT 1").fetchall()
#     return {"result": result}


# @app.get('/flashcard', response_model=FlashCardResponse)
# def get_flash_card():
#     return {
#     "questions": "What is the capital of France?",
#     "confidence": 0.9,
#     "notes": "Remember to review the landmarks of Paris."
# }

# @app.get('/materials', response_model=Materials)
# def get_flash_card():
#     return {
#     "type": "book",
#     "author": "John Doe",
#     "book_name": "Introduction to Python",
#     "platform": "udemy"
# }

# @app.get('/model', response_model=Subject)
# def get_flash_card():

#     return {
#     "content_from": "Introduction to Python Programming",
#     "study_material": {
#         "type": "book",
#         "author": "John Doe",
#         "book_name": "Learning Python"
#     },
#     "continuations": ["Advanced Python", "Data Science with Python"],
#     "flashcards": [
#         {
#             "questions": "What is a list in Python?",
#             "confidence": 0.8,
#             "notes": "Lists are mutable sequences in Python."
#         },
#         {
#             "questions": "How do you define a function in Python?",
#             "confidence": 0.9,
#             "notes": "Use the 'def' keyword to define a function."
#         }
#     ]
# }

# GET all flashcards
@app.get("/flashcards/", response_model=list[FlashCardCreate])
def get_flashcards(db: Session = Depends(get_db)):
    flashcards = db.query(FlashCard).all()

    if not flashcards:
        return {}
    
    return flashcards

@app.post("/flashcards/", response_model=FlashCardCreate)
def create_flashcard(flashcard: FlashCardCreate, db: Session = Depends(get_db)):

    # Convert the flashcard schema to a dictionary using model_dump()
    flashcard_data = flashcard.model_dump()

    new_flashcard = FlashCard(**flashcard_data)
    db.add(new_flashcard)
    db.commit()
    db.refresh(new_flashcard)

    return new_flashcard