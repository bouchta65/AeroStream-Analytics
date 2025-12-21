from sqlalchemy import create_engine, text
from datetime import datetime
import os

DB_URL = "postgresql://aerostream:aerostream@postgres:5432/aerostream"
engine = create_engine(DB_URL)


def init_db():
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS tweets (
                id SERIAL PRIMARY KEY,
                sentiment VARCHAR(50),
                confidence FLOAT,
                airline VARCHAR(100),
                negativereason VARCHAR(255),
                created_at TIMESTAMP,
                text TEXT
            )
        """))
        conn.commit()

