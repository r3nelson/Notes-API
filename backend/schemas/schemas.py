from pydantic import BaseModel
from typing import Optional, List

class FlashCardCreate(BaseModel):
    question: str
    confidence: float
    answer: str
    # subject_id: int # Foreign key reference to Subject
    subject_name: str

class FlashCardResponse(BaseModel):
    id: int
    question: str
    confidence: float
    answer: str
    subject_id: int  # This should be included to show the relationship
    class Config:
        orm_mode = True

class SubjectCreate(BaseModel):
    name: str
    continuations: Optional[List[str]] = []

class SubjectResponse(BaseModel):
    id: int
    name: str
    continuations: Optional[List[str]] = []
    class Config:
        orm_mode = True
