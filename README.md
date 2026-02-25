
# 📦 DONORGIS - Sustainable Donation Management System

A web-based platform that connects donors, NGOs, and donation centers to make the process of donating items simple, trackable, and geographically aware.

---

## 📖 Overview

DONORGIS was built to solve a real problem: people want to donate items like clothes, food, and hygiene products, but don't know where to go or how to coordinate with NGOs efficiently.

The system allows donors to register donations, NGOs to organize collection events, and everyone to visualize donation center locations on an interactive map. Geographic data for donation centers is pulled directly from OpenStreetMap using the Overpass API, making the locations real and up to date.

---

## ✨ Features

| Feature | Description |
|---|---|
| 👤 **User Management** | Create, edit, and delete donor profiles with email validation |
| 🤝 **NGO Profiles** | View registered NGOs and their contact information |
| 🗺️ **Interactive Map** | Leaflet.js map showing all donation centers with clickable markers |
| 📋 **Donation Tracking** | Register donations with item type, size, quantity, and status |
| 🎯 **NGO Events** | Collection drives with item targets, quantities, and date ranges |
| 🔍 **Available Filter** | Filter donations by "Available" status with a single checkbox |
| 🌍 **Geospatial Data** | Centers stored as PostGIS geometry, queried with ST_Transform |
| 🔄 **ETL Pipeline** | Real supermarket locations in Lisbon loaded from OpenStreetMap |

---

## 🗂️ Folder Structure

```
GPSoPA/
├── API/
│   ├── main.py          # API routes and app entry point
│   ├── models.py        # Database table definitions (SQLAlchemy)
│   ├── crud.py          # Database query functions
│   ├── schemas.py       # Data validation (Pydantic)
│   ├── database.py      # Database connection setup
│   ├── config.py        # Environment variable loading
│   ├── templates/
│   │   └── index.html   # Main frontend page
│   └── static/
│       ├── script.js    # Frontend logic and API calls
│       └── style.css    # Styling
├── ETL/
│   └── etl_donation_centers.py   # OpenStreetMap data pipeline
├── db/
│   ├── db.sql           # Full database schema
│   └── sampledata.sql   # Sample data for testing
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

| Component | Technology |
|---|---|
| Backend | FastAPI (Python) |
| Database | PostgreSQL + PostGIS |
| ORM | SQLAlchemy |
| Data Validation | Pydantic |
| Frontend | HTML, CSS, JavaScript |
| Map Rendering | Leaflet.js + OpenStreetMap |
| ETL Pipeline | Python + Overpass API |
| Environment Config | python-dotenv |

---

## 💻 Installation & Setup

1. **Clone the repository.**

```bash
git clone https://github.com/SolidAwesome/GPSoPA
cd GPSoPA
```

2. **Create and activate a virtual environment.**

Using conda:
```bash
conda create -n gpsopa python=3.10
conda activate gpsopa
```

Or using pip:
```bash
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Database setup.**

Make sure PostgreSQL with PostGIS is installed, then run:

```bash
psql -U postgres -f db/db.sql
psql -U postgres -d sustainable_donation -f db/sampledata.sql
```

5. **Environment setup.**

Create a `.env` file inside the `API/` folder:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sustainable_donation
DB_USER=postgres
DB_PASSWORD=your_password_here
```

> ⚠️ This file is git-ignored.

6. **ETL process**

Loads real donation center locations from OpenStreetMap:

```bash
cd ETL
python etl_donation_centers.py
```

---

7. **Run the application.**

```bash
cd API
uvicorn main:app --reload
```

The app will be available at: **http://localhost:8000**
API documentation at: **http://localhost:8000/docs**

----

## 🗄️ Database

PostgreSQL and PostGIS are used for spatial data storage and querying.

| Table | Description |
|---|---|
| `donation.users` | Donor profiles (name, role, contact) |
| `donation.ngo` | NGO registry (name, registration number, contact) |
| `donation.donation_centers` | Physical drop-off locations with PostGIS geometry |
| `donation.ngo_center` | Links NGOs to the centers they operate from |
| `donation.donations` | Individual donation records with status tracking |
| `donation.donation_items` | Item catalog (subcategory + target group + unit) |
| `donation.events` | NGO-organized collection drives |
| `donation.donation_status` | Status values: Available, Reserved, Collected |

---

## 🚀 API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Main dashboard (HTML) |
| `/users` | GET | List all users |
| `/users` | POST | Create a new user |
| `/users/{id}` | PUT | Update a user's contact |
| `/users/{id}` | DELETE | Delete a user |
| `/ngos` | GET | List all NGOs |
| `/donation_centers` | GET | List centers (id, name, city) |
| `/donation_centers_map` | GET | Centers with lat/lng for map |
| `/events` | GET | List all NGO events |
| `/donations` | GET | List all donations |
| `/donations?only_available=true` | GET | Filter available donations only |

---

## 📊 Results & Conclusions

The system successfully delivers a full-stack donation management platform combining relational data, geospatial queries, a REST API, and an interactive web frontend.

### ✅ What Worked Well

- The normalized PostgreSQL + PostGIS schema handles the full donation lifecycle cleanly, from item classification to status tracking
- FastAPI provides validated, auto-documented endpoints out of the box
- The ETL pipeline pulls real-world data from OpenStreetMap, making the map genuinely useful rather than fictional sample data
- The Leaflet.js map gives a spatial dimension to the data — users can visually locate nearby donation centers
- The dashboard supports full CRUD for users without needing any external admin tool

### ⚠️ Limitations & What Didn't Go as Planned

- **No authentication** — any user can edit or delete any record; this was planned but not implemented within the project timeline
- **Role input is not user-friendly** — the user creation form requires typing a role integer ID instead of selecting from a dropdown
- **Events are read-only** — NGOs can view events but cannot create or manage them from the dashboard
- **ETL uses hardcoded credentials** — unlike the rest of the app, the ETL script does not read from `.env`; this inconsistency was noticed late and not resolved
- **No frontend error feedback** — if a form submission fails (e.g. duplicate email), the user sees no error message — it just silently fails
- **Leaflet map re-initialization bug** — navigating away and back causes the map to not reload due to a stale `window.mapInitialized` flag; a workaround is in place but it is not a clean solution
- **Dead code in `crud.py`** — an unreachable `return result` statement was left after `get_centers()` by mistake

---

## 🔭 Next Steps

1. **User authentication** — implement login/logout with JWT tokens so only authorized users can write data
2. **Role-based access control** — restrict endpoints by user role (donor vs. NGO admin vs. system admin)
3. **NGO self-management** — allow NGOs to create and update their own events and manage donation statuses
4. **Donor-facing donation form** — a public form where donors can register a donation and pick a nearby center from the map
5. **ETL improvements** — move credentials to `.env`, schedule weekly runs, and extend coverage beyond Lisbon
6. **Nearest center query** — add a "find nearest center" endpoint using PostGIS `ST_Distance`
7. **Data visualizations** — add charts for donations by category and event progress using Chart.js
8. **Docker** — containerize the full stack so it can be launched with a single `docker-compose up`

---

## 👥 Group Members
- Afonso Couchinho
- Deni Ahmetaj
- Dora Šakić

---

*GPSoPA — NOVA IMS, Master's of Science in Geospatial Technologies