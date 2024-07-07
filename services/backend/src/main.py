from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # NEW

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from ..src.models import william

app = FastAPI()

# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#DB CONFIGURATION
SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://user:secret@db:5432/devdb'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind= engine)

Base = declarative_base()


#APIS
@app.get("/")
def home():
    return "Hello, World!"

@app.get("/test")
def test():
    db = SessionLocal()
    try:
        yield db
        #return engine.url.database
    finally:
        db.close()

@app.get("/william")
def williamTest():
    print(william)