# schemas.py
from pydantic import BaseModel, EmailStr

from pydantic import BaseModel
from typing import Optional
from datetime import date

# -------------------
# User Schema
# -------------------
class UserResponse(BaseModel):
    userid: int
    username: str
    contact: str

    class Config:
        from_attributes = True  # allows SQLAlchemy model -> Pydantic


class UserUpdate(BaseModel):
    username: Optional[str] = None
    userrole: Optional[int] = None
    contact: Optional[str] = None

    class Config:
        orm_mode = True

# -------------------
# NGO Schema
# -------------------
class NGOResponse(BaseModel):
    ngoid: int
    ngoname: str
    contact: str

    class Config:
        from_attributes = True

# -------------------
# Donation Center Schema
# -------------------
class DonationCenterResponse(BaseModel):
    centerid: int
    centername: str
    street: str
    city: str
    postalcode: str
    # Optional: geolocation if you want to include it later

    class Config:
        from_attributes = True

# -------------------
# Donation Status Schema
# -------------------
class DonationStatusResponse(BaseModel):
    statusid: int
    donationstatus: str

    class Config:
        from_attributes = True

# -------------------
# Donation Item Schema
# -------------------
class DonationItemResponse(BaseModel):
    itemid: int
    subcategoryid: int
    unitid: int
    targetgroupid: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    userrole: int
    contact: EmailStr

# -------------------
# Events Schema
# -------------------


class EventResponse(BaseModel):
    eventid: int
    eventname: str
    eventdescription: Optional[str]
    ngoid: int
    startdate: date
    enddate: Optional[date]
    eventtarget: int
    quantitytarget: int

    class Config:
        orm_mode = True