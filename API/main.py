# main.py
from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session, joinedload
from typing import List
from functools import lru_cache
import os

from database import SessionLocal
import crud
from models import DonationItem, Donation, DonationStatus
from schemas import UserResponse, NGOResponse, EventResponse, UserCreate, UserUpdate


app = FastAPI(title="Sustainable Donation API")

# --- Database dependency ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Templates + static files ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# --- Frontend route ---
@app.get("/", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# --- Users API ---
@app.get("/users", response_model=List[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user.username, user.userrole, user.contact)

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updated_user = crud.update_user_contact(db, user_id, user.contact)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = crud.delete_user(db, user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"User {user_id} deleted successfully"}

# --- NGOs API ---
@app.get("/ngos", response_model=List[NGOResponse])
def list_ngos(db: Session = Depends(get_db)):
    return crud.get_ngos(db)

# --- Donation Centers ---

@app.get("/donation_centers")
def donation_centers_list(db: Session = Depends(get_db)):
    centers = crud.get_centers(db)
    return [
        {
            "centerid": c.centerid,
            "centername": c.centername,
            "city": c.city
        }
        for c in centers
    ]


@app.get("/donation_centers_map")
def donation_centers_map(db: Session = Depends(get_db)):
    return crud.get_centers_map(db)

# --- Events API ---
@app.get("/events", response_model=List[EventResponse])
def list_events(db: Session = Depends(get_db)):
    return crud.get_events(db)

# --- Donation Items API ---
'''
@app.get("/donation_items")
def list_donation_items(db: Session = Depends(get_db)):
    items = crud.get_items(db)
    return [f"Item {i.itemid}" for i in items]
'''

# --- Donations API ---
@app.get("/donations")
def list_donations(only_available: bool = False, db: Session = Depends(get_db)):
    query = (
        db.query(Donation)
        .options(
            joinedload(Donation.item).joinedload(DonationItem.subcategory),
            joinedload(Donation.item).joinedload(DonationItem.target_group),
            joinedload(Donation.size),
            joinedload(Donation.status),
        )
    )
    if only_available:
        query = query.join(Donation.status).filter(DonationStatus.donationstatus == "Available")

    donations = query.all()
    return [
        {
            "subcategory": d.item.subcategory.subcategoryname if d.item and d.item.subcategory else "—",
            "target_group": d.item.target_group.groupname if d.item and d.item.target_group else "—",
            "size": d.size.productsize if d.size else "—",
            "quantity": d.quantity,
            "status": d.status.donationstatus if d.status else "—",
        }
        for d in donations
    ]