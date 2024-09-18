from pydantic import BaseModel
from typing import Optional, List

class FlashCardCreate(BaseModel):
    question: str
    confidence: float
    answer: str
    subject_id: int # Foreign key reference to Subject

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
    continuations: Optional[List[str]] = None
    # study_material: Optional[List[MaterialsCreate]] = None  
    # flashcards: Optional[List[FlashCardCreate]] = None

class SubjectResponse(BaseModel):
    id: int
    name: str
    continuations: Optional[List[str]] = None
    # study_material: Optional[List[MaterialsResponse]] = None    
    
    # flashcards: Optional[List[FlashCardResponse]] = None # this field isn't necessary as long as we can match flashcard by subject_id

    class Config:
        orm_mode = True

# class MaterialsCreate(BaseModel):
#     type: str # book, online course, etc.
#     author: Optional[str] = None
#     book_name: Optional[str] = None
#     course: Optional[str] = None
#     course_name: Optional[str] = None
#     platform: Optional[str] = None # udemy, INE, etc.
#     subject_id: int  # Foreign key reference to Subject

# class MaterialsResponse(BaseModel):
#     id: int
#     type: str # book, online course, etc.
#     author: Optional[str] = None
#     book_name: Optional[str] = None
#     course: Optional[str] = None
#     course_name: Optional[str] = None
#     platform: Optional[str] = None # udemy, INE, youtube etc.
#     subject: Optional["SubjectResponse"]  # Include the associated subject

    # class Config:
    #     orm_mode = True