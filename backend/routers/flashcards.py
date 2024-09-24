from fastapi import APIRouter, Depends, HTTPException
from schemas.schemas import FlashCardCreate, FlashCardResponse
from sqlalchemy.orm import Session
from models.models import FlashCard
from typing import List, Optional
from db.database import get_db
from .subjects import get_subject_id, get_subject

router = APIRouter()

def subject_id_validator (db: Session, subject_id: int = None, subject_name: str = None):
    if not subject_id and not subject_name: raise HTTPException(status_code=400, detail="Subject_id or Subject_name is required and both cannot be empty")
    elif subject_id: return get_subject(db=db, subject_id=subject_id).id
    elif subject_name:
        return get_subject_id(db=db, subject_name= subject_name.lower())["subject.id"] 

def question_validator(question: str):
    if not question:  raise HTTPException(status_code=400, detail="Question is required and cannot be empty")
    return question.lower()

def confidence_validator(confidence: float):
    if not confidence: raise HTTPException(status_code=400, detail="Confidence is required and cannot be empty")
        
    if confidence < 1.0 or confidence > 10.0:
        raise HTTPException(status_code=400, detail="Confidence must be between 1.0 and 10.0.")
    
    return round(confidence * 2) / 2 # round values to .5 (e.g. 7.0, 7.5, 8.0, 8.5, etc.)

def answer_validator(answer: str):
    if not answer: raise HTTPException(status_code=400, detail="Answer is required and cannot be empty")
    return answer.lower()

# GET all flashcards
@router.get("/flashcards/", response_model=list[FlashCardResponse])
def get_all_flashcards(db: Session = Depends(get_db)):
    flashcards = db.query(FlashCard).all()

    if not flashcards:
        return []
    return flashcards

# GET a flashcard by id
@router.get("/flashcard/{flashcard_id}", response_model=FlashCardResponse)
def get_flashcard(flashcard_id: int, db: Session = Depends(get_db)):
    flashcard = db.query(FlashCard).filter(FlashCard.id == flashcard_id).first()

    if not flashcard:
        raise HTTPException(status_code=404, detail="Flashcard not found")
    
    return flashcard

@router.get("/flashcards/{subject_name}")
def get_flashcards_by_subject(subject_name: str, db: Session = Depends(get_db)):
    subject_id = subject_id_validator(db=db, subject_name=subject_name)
    flashcards = db.query(FlashCard).filter(FlashCard.subject_id == subject_id).all()

    if not flashcards:
        raise HTTPException(status_code=404, detail=f"No flashcards found for {subject_name}")
    return flashcards

# POST a flashcard by id
@router.post("/flashcards/", response_model=FlashCardResponse)
def create_flashcard(
                    flashcard: FlashCardCreate,
                    question: str = None,
                    answer: str = None,
                    confidence: float = 1.0,
                    subject_id: int = None,
                    subject_name: str = None,
                    db: Session = Depends(get_db)):
    
    if not question and flashcard.question: question = flashcard.question
    if not answer and flashcard.answer: answer = flashcard.answer
    if not confidence and flashcard.confidence: confidence = flashcard.confidence
    if not subject_id and flashcard.subject_id: subject_id = flashcard.subject_id
    if not subject_name and flashcard.subject_name: subject_name = flashcard.subject_name
    
    subject_id = subject_id_validator(db=db,subject_id=subject_id, subject_name=subject_name)
    question = question_validator(question)
    confidence = confidence_validator(confidence)
    answer = answer_validator(answer)
    
    new_flashcard = FlashCard(
        question=question,
        answer=answer,
        confidence=confidence,
        subject_id=subject_id
    )
    
    db.add(new_flashcard)
    db.commit()
    db.refresh(new_flashcard)

    return new_flashcard

# Patch a flashcard by id
@router.patch("/flashcard/{flashcard_id}", response_model=FlashCardCreate)
def update_flashcard(flashcard_id: int, question: str = None, confidence: float = None, answer: str = None, db: Session = Depends(get_db)):

    flashcard = db.query(FlashCard).filter(FlashCard.id == flashcard_id).first()

    if not flashcard:
        raise HTTPException(status_code=404, detail="Flashcard not found")

    if question:
        flashcard.question = question.lower()
    if confidence:
        flashcard.confidence = confidence
    if answer:
        flashcard.answer = answer.lower()

    db.commit()
    db.refresh(flashcard)
    return flashcard


# Delete a flashcard by id
@router.delete("/flashcard/{flashcard_id}")
def get_flashcard(flashcard_id: int, db: Session = Depends(get_db)):
    flashcard = db.query(FlashCard).filter(FlashCard.id == flashcard_id).first()

    if not flashcard:
        raise HTTPException(status_code=404, detail="Flashcard not found")
    
    db.delete(flashcard)
    db.commit()
    
    return {"FlashCard successfully deleted": f"{repr(flashcard)}"}