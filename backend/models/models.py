from pydantic import BaseModel
from typing import Optional, List

class FlashCard(BaseModel):
    questions: str
    confidence: float
    notes: str

class Materials(BaseModel):
    type: str # book, online course, etc.
    author: Optional[str] = None
    book_name: Optional[str] = None
    course: Optional[str] = None
    course_name: Optional[str] = None
    platform: Optional[str] = None # udemy, INE, etc.

class Subject(BaseModel):
    content_from: str
    study_material: Materials  
    continuations:Optional[list] = None
    flashcards: List[FlashCard]