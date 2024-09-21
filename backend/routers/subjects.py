from fastapi import APIRouter, Depends, HTTPException
from schemas.schemas import  SubjectResponse, SubjectCreate
from sqlalchemy.orm import Session
from models.models import Subject
from typing import List, Optional
from db.database import get_db

router = APIRouter()

# GET all subjects
@router.get("/subjects/", response_model=list[SubjectResponse])
def get_all_subjects(db: Session = Depends(get_db)):
    subjects = db.query(Subject).all()

    if not subjects:
        return []
    return subjects

# GET a subject by id
@router.get("/subject/{id}", response_model=SubjectResponse)
def get_subject(id: int, db: Session = Depends(get_db)):
    subject = db.query(Subject).filter(Subject.id == id).first()

    if not subject:
        raise HTTPException(status_code=404, detail=f"No subject with id '{id}' found")
    
    return subject

# GET a subject id by subject name
@router.get("/subject/id/{subject_name}")
def get_subject_id(subject_name: str, db: Session = Depends(get_db)):
    subject = db.query(Subject).filter(Subject.name == subject_name).first()

    if not subject:
        raise HTTPException(status_code=404, detail=f"Subject '{subject_name}' not found")
    return {"subject.id" : subject.id}


@router.post("/subjects/", response_model=SubjectResponse)
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

