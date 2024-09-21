from fastapi import APIRouter, Depends, HTTPException
from schemas.schemas import FlashCardCreate, FlashCardResponse
from sqlalchemy.orm import Session
from models.models import FlashCard
from typing import List, Optional
from db.database import get_db
from .subjects import get_subject_id

router = APIRouter()

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
    subject_id = get_subject_id(subject_name, db=db)["subject.id"]
    flashcards = db.query(FlashCard).filter(FlashCard.subject_id == subject_id).all()

    if not flashcards:
        raise HTTPException(status_code=404, detail=f"No flashcards found for {subject_name}")
    return flashcards

# POST a flashcard by id
@router.post("/flashcards/", response_model=FlashCardResponse)
def create_flashcard(
                    question: str,
                    answer: str,
                    confidence: float = 1.0,
                    subject_id: int = None,
                    subject_name: str = None,
                    db: Session = Depends(get_db)):
    
    if confidence < 1.0 or confidence > 10.0:
        raise HTTPException(status_code=400, detail="Confidence must be between 1.0 and 10.0.")
    
    if not subject_id and not subject_name: raise HTTPException(status_code=400, detail="Subject_id or Subject_name is required and both cannot be empty")

    if not subject_id and subject_name:
        subject_id  = get_subject_id(subject_name, db=db)["subject.id"] # returns {"subject.id": number}

    if not question:  raise HTTPException(status_code=400, detail="Question is required and cannot be empty")
    if not confidence: raise HTTPException(status_code=400, detail="Confidence is required and cannot be empty")
    if not answer: raise HTTPException(status_code=400, detail="Answer is required and cannot be empty")

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
        flashcard.question = question
    if confidence:
        flashcard.confidence = confidence
    if answer:
        flashcard.answer = answer

    db.commit()
    db.refresh(flashcard)
    return flashcard


