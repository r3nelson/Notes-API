from sqlalchemy import Column, Integer, String, Float
from db.database import Base

class FlashCard(Base):
    __tablename__ = "flashcards"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    confidence = Column(Float,nullable= False)
    answer = Column(String, nullable=False)
