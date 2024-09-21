from sqlalchemy import Column, Integer, String, Float, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.types import TypeDecorator, Text
from db.database import Base
from typing import List, Optional
import json

class JSONType(TypeDecorator):
    impl = Text

    def process_bind_param(self, value, dialect):
        if isinstance(value, list):
            # convert list to string
            return json.dumps(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            # convert str to dict
            return json.loads(value)
        return value
    
class FlashCard(Base):
    __tablename__ = "flashcards"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    confidence = Column(Float,nullable= False)
    answer = Column(String, nullable=False)

     # Foreign key reference to Subject
    subject_id = Column(Integer, ForeignKey('subjects.id'))

    # Define relationship back to Subject
    subject = relationship("Subject", back_populates="flashcards")

    __table_args__ = (
        CheckConstraint('confidence >= 1.0', name='check_confidence_min'),
        CheckConstraint('confidence <= 10.0', name='check_confidence_max'),
    )

    def __init__(self, question:str, confidence: float, answer: str, subject_id: int):
        self.question = question.lower() 
        self.confidence = confidence
        self.answer = answer.lower()
        self.subject_id = subject_id
    
    def __repr__(self):
        return f"FlashCard(id={self.id}, question={self.question}, confidence={self.confidence}, answer={self.answer}, subject_id={self.subject_id})"
    
class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    continuations = Column(JSONType, nullable=True)
    # study_material = relationship("Materials", back_populates="subject")  # Updated to reflect the relationship
    
    # Define the relationship to flashcards
    flashcards = relationship("FlashCard", back_populates="subject", cascade="all, delete-orphan")

    def __init__ (self, name:str, continuations: Optional[List[str]] = None):
        self.name = name.lower
        self.continuations = [c.lower() for c in continuations] if continuations else None
    
    def __repr__(self):
        return f"Subject(id={self.id}, name={self.name}, continuations={self.continuations})"

# class Materials(Base):
#     __tablename__ = "materials"

#     id = Column(Integer, primary_key=True, index=True)
#     type = Column(String, nullable=False)  # book, online course, etc.
#     author = Column(String, nullable=True)
#     book_name = Column(String, nullable=True)
#     course = Column(String, nullable=True)
#     course_name = Column(String, nullable=True)
#     platform = Column(String, nullable=True)  # udemy, INE, etc.
#     subject_id = Column(Integer, ForeignKey('subjects.id'))  # Foreign key reference to Subject

#     # Define the relationship to Subject
#     subject = relationship("Subject", back_populates="study_material")
