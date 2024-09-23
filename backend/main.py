from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import flashcards
from routers import subjects
from db.database import  init_db

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # might change to specify frontend # allow_origins=["http://localhost:3000"] 
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  
)

# initalize database
init_db()

app.include_router(flashcards.router, prefix="/api", tags=["Flashcards"])
app.include_router(subjects.router, prefix="/api", tags=["Subjects"])


