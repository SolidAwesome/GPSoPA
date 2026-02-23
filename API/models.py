from sqlalchemy import Column, Integer, String, Date, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from database import Base

# --- Units ---
class Unit(Base):
    __tablename__ = "units"
    __table_args__ = {"schema": "donation"}

    unitid = Column(Integer, primary_key=True)
    unitname = Column(String(20), nullable=False, unique=True)


# --- Target Groups ---
class TargetGroup(Base):
    __tablename__ = "target_groups"
    __table_args__ = {"schema": "donation"}

    targetgroupid = Column(Integer, primary_key=True)
    groupname = Column(String(50), nullable=False, unique=True)


# --- Categories ---
class Category(Base):
    __tablename__ = "categories"
    __table_args__ = {"schema": "donation"}

    categoryid = Column(Integer, primary_key=True)
    categoryname = Column(String(100), nullable=False, unique=True)


# --- Subcategories ---
class Subcategory(Base):
    __tablename__ = "subcategories"
    __table_args__ = {"schema": "donation"}

    subcategoryid = Column(Integer, primary_key=True)
    subcategoryname = Column(String(300), nullable=False)
    categoryid = Column(Integer, ForeignKey("donation.categories.categoryid", ondelete="CASCADE"), nullable=False)

    category = relationship("Category")


# --- Donation Items ---
class DonationItem(Base):
    __tablename__ = "donation_items"
    __table_args__ = {"schema": "donation"}

    itemid = Column(Integer, primary_key=True)
    subcategoryid = Column(Integer, ForeignKey("donation.subcategories.subcategoryid", ondelete="RESTRICT"), nullable=False)
    unitid = Column(Integer, ForeignKey("donation.units.unitid", ondelete="RESTRICT"), nullable=False)
    targetgroupid = Column(Integer, ForeignKey("donation.target_groups.targetgroupid", ondelete="RESTRICT"), nullable=False)

    subcategory = relationship("Subcategory")
    unit = relationship("Unit")
    target_group = relationship("TargetGroup")


# --- Donation Status ---
class DonationStatus(Base):
    __tablename__ = "donation_status"
    __table_args__ = {"schema": "donation"}

    statusid = Column(Integer, primary_key=True)
    donationstatus = Column(String(50), nullable=False, unique=True)


# --- User Type ---
class UserType(Base):
    __tablename__ = "usertype"
    __table_args__ = {"schema": "donation"}

    usertypeid = Column(Integer, primary_key=True)
    userrole = Column(String(20), nullable=False, unique=True)


# --- Users ---
class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "donation"}

    userid = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    userrole = Column(Integer, ForeignKey("donation.usertype.usertypeid"), nullable=False)
    contact = Column(String(100), nullable=False, unique=True)
    created = Column(Date)

    role = relationship("UserType")


# --- NGO ---
class NGO(Base):
    __tablename__ = "ngo"
    __table_args__ = {"schema": "donation"}

    ngoid = Column(Integer, primary_key=True)
    ngoname = Column(String(150), nullable=False, unique=True)
    registrationnumber = Column(String(100), nullable=False, unique=True)
    contact = Column(String(100), nullable=False, unique=True)


# --- Donation Centers ---
class DonationCenter(Base):
    __tablename__ = "donation_centers"
    __table_args__ = {"schema": "donation"}

    centerid = Column(Integer, primary_key=True)
    centername = Column(String(150), nullable=False)
    street = Column(String(150), nullable=False)
    city = Column(String(100), nullable=False)
    postalcode = Column(String(50), nullable=False)
    geolocation = Column(Geometry("POINT", srid=4326), nullable=False)


# --- NGO Centers ---
class NGOCenter(Base):
    __tablename__ = "ngo_center"
    __table_args__ = {"schema": "donation"}

    ngocenterid = Column(Integer, primary_key=True)
    ngoid = Column(Integer, ForeignKey("donation.ngo.ngoid", ondelete="CASCADE"), nullable=False)
    centerid = Column(Integer, ForeignKey("donation.donation_centers.centerid", ondelete="CASCADE"), nullable=False)

    ngo = relationship("NGO")
    center = relationship("DonationCenter")


# --- Events ---
class Event(Base):
    __tablename__ = "events"
    __table_args__ = {"schema": "donation"}

    eventid = Column(Integer, primary_key=True)
    eventname = Column(String(150), nullable=False)
    eventdescription = Column(String(150))
    ngoid = Column(Integer, ForeignKey("donation.ngo.ngoid", ondelete="CASCADE"), nullable=False)
    startdate = Column(Date, nullable=False)
    enddate = Column(Date)
    eventtarget = Column(Integer, ForeignKey("donation.donation_items.itemid"), nullable=False)
    quantitytarget = Column(Integer, nullable=False)

    __table_args__ = (CheckConstraint("quantitytarget >= 0"), {"schema": "donation"})

    ngo = relationship("NGO")
    donation_item = relationship("DonationItem")


# --- Sizes ---
class Size(Base):
    __tablename__ = "sizes"
    __table_args__ = {"schema": "donation"}

    sizeid = Column(Integer, primary_key=True)
    productsize = Column(String(10), nullable=False, unique=True)


# --- Donations ---
class Donation(Base):
    __tablename__ = "donations"
    __table_args__ = {"schema": "donation"}

    id = Column(Integer, primary_key=True)
    userid = Column(Integer, ForeignKey("donation.users.userid"), nullable=False)
    ngocenterid = Column(Integer, ForeignKey("donation.ngo_center.ngocenterid"), nullable=False)
    itemid = Column(Integer, ForeignKey("donation.donation_items.itemid"), nullable=False)
    sizeid = Column(Integer, ForeignKey("donation.sizes.sizeid"))
    quantity = Column(Integer, nullable=False)
    donationdescription = Column(String(150))
    eventid = Column(Integer, ForeignKey("donation.events.eventid"))
    statusid = Column(Integer, ForeignKey("donation.donation_status.statusid"), nullable=False)
    donationdate = Column(Date)

    __table_args__ = (CheckConstraint("quantity > 0"), {"schema": "donation"})

    user = relationship("User")
    center = relationship("NGOCenter")
    item = relationship("DonationItem")
    size = relationship("Size")
    event = relationship("Event")
    status = relationship("DonationStatus")