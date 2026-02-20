from datetime import date
from sqlalchemy import (
    Column, Integer, String, Date, ForeignKey, UniqueConstraint, CheckConstraint
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import create_engine
from geoalchemy2 import Geometry

from config import DATABASE_URL

# Base is the "parent class" for all models
# Think of it as a template that every table inherits from
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


# -------------------------------------------------------
# LOOKUP TABLES
# These are simple tables that store fixed options
# Like dropdown menus in a form
# -------------------------------------------------------

class Unit(Base):
    """Units of measurement: kg, piece, pair, pack"""
    __tablename__ = "units"
    __table_args__ = {"schema": "donation"}

    unitid = Column(Integer, primary_key=True, index=True)
    unitname = Column(String(20), nullable=False, unique=True)

    # Relationship: one unit can be used in many donation items
    donation_items = relationship("DonationItem", back_populates="unit")


class TargetGroup(Base):
    """Target groups: General, Male, Female, Children, Baby"""
    __tablename__ = "target_groups"
    __table_args__ = {"schema": "donation"}

    targetgroupid = Column(Integer, primary_key=True, index=True)
    groupname = Column(String(50), nullable=False, unique=True)

    donation_items = relationship("DonationItem", back_populates="target_group")


class Category(Base):
    """Main categories: Food, Clothing, Shoes, Hygiene Products, Household"""
    __tablename__ = "categories"
    __table_args__ = {"schema": "donation"}

    categoryid = Column(Integer, primary_key=True, index=True)
    categoryname = Column(String(100), nullable=False, unique=True)

    # Relationship: one category has many subcategories
    subcategories = relationship("Subcategory", back_populates="category")


class Subcategory(Base):
    """Subcategories: e.g. T-shirts, Sneakers, Soap (belong to a Category)"""
    __tablename__ = "subcategories"
    __table_args__ = (
        UniqueConstraint("subcategoryname", "categoryid"),
        {"schema": "donation"}
    )

    subcategoryid = Column(Integer, primary_key=True, index=True)
    subcategoryname = Column(String(300), nullable=False)
    categoryid = Column(Integer, ForeignKey("donation.categories.categoryid"), nullable=False)

    # Relationships
    category = relationship("Category", back_populates="subcategories")
    donation_items = relationship("DonationItem", back_populates="subcategory")


class DonationStatus(Base):
    """Donation statuses: Available, Reserved, Collected"""
    __tablename__ = "donation_status"
    __table_args__ = {"schema": "donation"}

    statusid = Column(Integer, primary_key=True, index=True)
    donationstatus = Column(String(50), nullable=False, unique=True)

    donations = relationship("Donation", back_populates="status")


class UserType(Base):
    """User roles: donor, ngo admin, admin"""
    __tablename__ = "usertype"
    __table_args__ = {"schema": "donation"}

    usertypeid = Column(Integer, primary_key=True, index=True)
    userrole = Column(String(20), nullable=False, unique=True)

    users = relationship("User", back_populates="usertype")


class Size(Base):
    """Sizes: XS, S, M, L, XL, XXL, 37, 38, 39... (for clothing and shoes)"""
    __tablename__ = "sizes"
    __table_args__ = {"schema": "donation"}

    sizeid = Column(Integer, primary_key=True, index=True)
    productsize = Column(String(10), nullable=False, unique=True)

    donations = relationship("Donation", back_populates="size")


# -------------------------------------------------------
# CORE TABLES
# These are the main tables with the important data
# -------------------------------------------------------

class DonationItem(Base):
    """
    Donation items: combination of subcategory + unit + target group
    Example: T-shirts (subcategory) + pair (unit) + Male (target group)
    """
    __tablename__ = "donation_items"
    __table_args__ = (
        UniqueConstraint("subcategoryid", "targetgroupid"),
        {"schema": "donation"}
    )

    itemid = Column(Integer, primary_key=True, index=True)
    subcategoryid = Column(Integer, ForeignKey("donation.subcategories.subcategoryid"), nullable=False)
    unitid = Column(Integer, ForeignKey("donation.units.unitid"), nullable=False)
    targetgroupid = Column(Integer, ForeignKey("donation.target_groups.targetgroupid"), nullable=False)

    # Relationships
    subcategory = relationship("Subcategory", back_populates="donation_items")
    unit = relationship("Unit", back_populates="donation_items")
    target_group = relationship("TargetGroup", back_populates="donation_items")
    donations = relationship("Donation", back_populates="item")
    events = relationship("Event", back_populates="target_item")


class User(Base):
    """Users of the system: donors, NGO admins, admins"""
    __tablename__ = "users"
    __table_args__ = {"schema": "donation"}

    userid = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    userrole = Column(Integer, ForeignKey("donation.usertype.usertypeid"), nullable=False)
    contact = Column(String(100), nullable=False, unique=True)
    created = Column(Date, default=date.today)

    # Relationships
    usertype = relationship("UserType", back_populates="users")
    donations = relationship("Donation", back_populates="user")


class NGO(Base):
    """NGO organizations: Green Future, Helping Hands, Hand in Hand"""
    __tablename__ = "ngo"
    __table_args__ = {"schema": "donation"}

    ngoid = Column(Integer, primary_key=True, index=True)
    ngoname = Column(String(150), nullable=False, unique=True)
    registrationnumber = Column(String(100), nullable=False, unique=True)
    contact = Column(String(100), nullable=False, unique=True)

    # Relationships
    ngo_centers = relationship("NGOCenter", back_populates="ngo")
    events = relationship("Event", back_populates="ngo")


class DonationCenter(Base):
    """Physical donation centers where items are dropped off"""
    __tablename__ = "donation_centers"
    __table_args__ = {"schema": "donation"}

    centerid = Column(Integer, primary_key=True, index=True)
    centername = Column(String(150), nullable=False)
    street = Column(String(150), nullable=False)
    city = Column(String(100), nullable=False)
    postalcode = Column(String(15), nullable=False)
    geolocation = Column(Geometry("POINT", srid=4326), nullable=False)

    ngo_centers = relationship("NGOCenter", back_populates="center")


class NGOCenter(Base):
    """
    Links NGOs to their donation centers (many-to-many)
    One NGO can have multiple centers, one center can belong to multiple NGOs
    """
    __tablename__ = "ngo_center"
    __table_args__ = (
        UniqueConstraint("ngoid", "centerid"),
        {"schema": "donation"}
    )

    ngocenterid = Column(Integer, primary_key=True, index=True)
    ngoid = Column(Integer, ForeignKey("donation.ngo.ngoid"), nullable=False)
    centerid = Column(Integer, ForeignKey("donation.donation_centers.centerid"), nullable=False)

    # Relationships
    ngo = relationship("NGO", back_populates="ngo_centers")
    center = relationship("DonationCenter", back_populates="ngo_centers")
    donations = relationship("Donation", back_populates="ngo_center")


class Event(Base):
    """Donation events/drives organized by NGOs"""
    __tablename__ = "events"
    __table_args__ = {"schema": "donation"}

    eventid = Column(Integer, primary_key=True, index=True)
    eventname = Column(String(150), nullable=False)
    eventdescription = Column(String(150))
    ngoid = Column(Integer, ForeignKey("donation.ngo.ngoid"), nullable=False)
    startdate = Column(Date, nullable=False)
    enddate = Column(Date)
    eventtarget = Column(Integer, ForeignKey("donation.donation_items.itemid"), nullable=False)
    quantitytarget = Column(Integer, nullable=False)

    # Relationships
    ngo = relationship("NGO", back_populates="events")
    target_item = relationship("DonationItem", back_populates="events")
    donations = relationship("Donation", back_populates="event")


class Donation(Base):
    """
    The main table — each row is one donation made by a user
    Links together: user, NGO center, item, size, event, status
    """
    __tablename__ = "donations"
    __table_args__ = (
        CheckConstraint("quantity > 0"),
        {"schema": "donation"}
    )

    id = Column(Integer, primary_key=True, index=True)
    userid = Column(Integer, ForeignKey("donation.users.userid"), nullable=False)
    ngocenterid = Column(Integer, ForeignKey("donation.ngo_center.ngocenterid"), nullable=False)
    itemid = Column(Integer, ForeignKey("donation.donation_items.itemid"), nullable=False)
    sizeid = Column(Integer, ForeignKey("donation.sizes.sizeid"), nullable=True)
    quantity = Column(Integer, nullable=False)
    donationdescription = Column(String(150))
    eventid = Column(Integer, ForeignKey("donation.events.eventid"), nullable=True)
    statusid = Column(Integer, ForeignKey("donation.donation_status.statusid"), nullable=False)
    donationdate = Column(Date, default=date.today)

    # Relationships
    user = relationship("User", back_populates="donations")
    ngo_center = relationship("NGOCenter", back_populates="donations")
    item = relationship("DonationItem", back_populates="donations")
    size = relationship("Size", back_populates="donations")
    event = relationship("Event", back_populates="donations")
    status = relationship("DonationStatus", back_populates="donations")


# -------------------------------------------------------
# DATABASE INITIALIZATION
# Run this once to create all tables
# -------------------------------------------------------
def init_db():
    """Creates all tables in the database."""
    Base.metadata.create_all(bind=engine)
