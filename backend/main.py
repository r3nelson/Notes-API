from fastapi import FastAPI
from models.models import FlashCard, Materials, Subject

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Hello World"}


@app.get('/flashcard', response_model=FlashCard)
def get_flash_card():
    return {
    "questions": "What is the capital of France?",
    "confidence": 0.9,
    "notes": "Remember to review the landmarks of Paris."
}

@app.get('/materials', response_model=Materials)
def get_flash_card():
    return {
    "type": "book",
    "author": "John Doe",
    "book_name": "Introduction to Python",
    "platform": "udemy"
}

@app.get('/model', response_model=Subject)
def get_flash_card():
    return {
    "content_from": "Introduction to Python Programming",
    "study_material": {
        "type": "book",
        "author": "John Doe",
        "book_name": "Learning Python"
    },
    "continuations": ["Advanced Python", "Data Science with Python"],
    "flashcards": [
        {
            "questions": "What is a list in Python?",
            "confidence": 0.8,
            "notes": "Lists are mutable sequences in Python."
        },
        {
            "questions": "How do you define a function in Python?",
            "confidence": 0.9,
            "notes": "Use the 'def' keyword to define a function."
        }
    ]
}