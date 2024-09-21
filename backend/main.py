from fastapi import FastAPI
from routers import flashcards
from routers import subjects
from db.database import  init_db

app = FastAPI()

# initalize database
init_db()

app.include_router(flashcards.router, prefix="/api", tags=["Flashcards"])
app.include_router(subjects.router, prefix="/api", tags=["Subjects"])


