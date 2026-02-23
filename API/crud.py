# crud.py
from sqlalchemy.orm import Session
from sqlalchemy import func
from models import User, NGO, DonationCenter, DonationItem, Event

# --- Users CRUD ---
def get_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.userid == user_id).first()

def create_user(db: Session, username: str, userrole: str, contact: str):
    new_user = User(username=username, userrole=userrole, contact=contact)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user_contact(db: Session, user_id: int, contact: str):
    user = get_user(db, user_id)
    if user:
        user.contact = contact
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
    return user

# --- NGOs CRUD ---
def get_ngos(db: Session):
    return db.query(NGO).all()

# --- Donation Centers CRUD ---

def get_centers_map(db: Session):
    centers = db.query(
        DonationCenter.centerid,
        DonationCenter.centername,
        DonationCenter.city,
        func.ST_X(func.ST_Transform(DonationCenter.geolocation, 4326)).label("lng"),
        func.ST_Y(func.ST_Transform(DonationCenter.geolocation, 4326)).label("lat")
    ).all()

    result = []
    for c in centers:
        result.append({
            "centerid": c.centerid,
            "centername": c.centername,
            "city": c.city,
            "lat": float(c.lat),
            "lng": float(c.lng)
        })

    return result


def get_centers(db: Session):
    return db.query(DonationCenter.centerid, DonationCenter.centername, DonationCenter.city).all()


    return result
# --- Events CRUD ---
def get_events(db: Session):
    return db.query(Event).all()

# --- Donation Items CRUD ---
def get_items(db: Session):
    return db.query(DonationItem).all()