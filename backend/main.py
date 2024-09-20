from fastapi import FastAPI, Depends, HTTPException
from schemas.schemas import FlashCardCreate, FlashCardResponse, SubjectResponse, SubjectCreate
from sqlalchemy.orm import Session
from db.database import SessionLocal, engine, Base, init_db
from models.models import FlashCard, Subject
from typing import List, Optional

app = FastAPI()
init_db()


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

# GET all flashcards
@app.get("/flashcards/", response_model=list[FlashCardResponse])
def get_flashcards(db: Session = Depends(get_db)):
    flashcards = db.query(FlashCard).all()

    if not flashcards:
        return []
    return flashcards

# GET a flashcard by id
@app.get("/flashcard/{flashcard_id}", response_model=FlashCardResponse)
def get_flashcard(flashcard_id: int, db: Session = Depends(get_db)):
    flashcard = db.query(FlashCard).filter(FlashCard.id == flashcard_id).first()

    if not flashcard:
        raise HTTPException(status_code=404, detail="Flashcard not found")
    
    return flashcard

# Patch a flashcard by id
@app.patch("/flashcard/{flashcard_id}", response_model=FlashCardCreate)
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

# GET all subjects
@app.get("/subjects/", response_model=list[SubjectResponse])
def get_subjects(db: Session = Depends(get_db)):
    subjects = db.query(Subject).all()

    if not subjects:
        return []
    return subjects

# GET a subject by id
@app.get("/subject/{id}", response_model=SubjectResponse)
def get_subject(id: int, db: Session = Depends(get_db)):
    subject = db.query(Subject).filter(Subject.id == id).first()

    if not subject:
        raise HTTPException(status_code=404, detail=f"No subject with id '{id}' found")
    
    return subject

# GET a subject id by subject name
@app.get("/subject/id/{subject_name}")
def get_subject_id(subject_name: str, db: Session = Depends(get_db)):
    subject = db.query(Subject).filter(Subject.name == subject_name).first()

    if not subject:
        raise HTTPException(status_code=404, detail=f"Subject '{subject_name}' not found")
    return {"subject.id" : subject.id}

# POST a flashcard by id
@app.post("/flashcards/", response_model=FlashCardResponse)
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

@app.post("/subjects/", response_model=SubjectResponse)
def create_subject(
                subject_name: str,
                continuations: Optional[List[str]] = None,
                db:Session = Depends(get_db)):

    if not subject_name:  raise HTTPException(status_code=400, detail="subject_name is required and cannot be empty")

    existing_subject = db.query(Subject).filter(Subject.name == subject_name).first()
    if existing_subject:
        raise HTTPException(status_code=400, detail=f"Subject '{subject_name}' already exists.")
    
    new_subject = Subject(
        subject_name=subject_name,
        continuations=continuations
    )

    db.add(new_subject)
    db.commit()
    db.refresh(new_subject)
    return new_subject

@app.get("/flashcards/{subject_name}")
def get_flashcards_by_subject(subject_name: str, db: Session = Depends(get_db)):
    subject_id = get_subject_id(subject_name, db=db)["subject.id"]
    flashcards = db.query(FlashCard).filter(FlashCard.subject_id == subject_id).all()

    if not flashcards:
        raise HTTPException(status_code=404, detail=f"No flashcards found for {subject_name}")
    return flashcards



