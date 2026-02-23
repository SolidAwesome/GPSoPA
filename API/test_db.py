from config import DATABASE_URL
from sqlalchemy import create_engine
engine = create_engine(DATABASE_URL)
with engine.connect() as conn:
    result = conn.execute("SELECT 1")
    print("DB connected!")
