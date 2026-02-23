from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import SessionLocal, User, NGO
from typing import List

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "API running"}


@app.get("/users")
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@app.get("/ngos")
def list_ngos(db: Session = Depends(get_db)):
    return db.query(NGO).all()
