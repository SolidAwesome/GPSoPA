from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List
import os

from database import SessionLocal
from models import User, NGO, DonationCenter, DonationStatus, DonationItem
from schemas import UserResponse, NGOResponse, DonationCenterResponse, UserCreate

app = FastAPI(title="Sustainable Donation API")

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Templates + static (relative paths)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Frontend route
@app.get("/", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# --- Users API ---
@app.get("/users", response_model=List[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        username=user.username,
        userrole=user.userrole,
        contact=user.contact
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.userid == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": f"User {user_id} deleted successfully"}

# --- NGOs API ---
@app.get("/ngos", response_model=List[NGOResponse])
def list_ngos(db: Session = Depends(get_db)):
    return db.query(NGO).all()

# --- Donation Centers API ---
@app.get("/donation_centers", response_model=List[DonationCenterResponse])
def list_centers(db: Session = Depends(get_db)):
    return db.query(DonationCenter).all()

# --- Donation Status API ---
@app.get("/donation_status", response_model=List[str])
def list_statuses(db: Session = Depends(get_db)):
    statuses = db.query(DonationStatus).all()
    return [s.donationstatus for s in statuses]

# --- Donation Items API ---
@app.get("/donation_items", response_model=List[str])
def list_donation_items(db: Session = Depends(get_db)):
    items = db.query(DonationItem).all()
    return [f"Item {i.itemid}" for i in items]