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


def save_tweet(tweet):
    with engine.connect() as conn:
        conn.execute(text("""
            INSERT INTO tweets
            (sentiment, confidence, airline, negativereason, created_at, text)
            VALUES (:sentiment, :confidence, :airline, :negativereason, :created_at, :text)
        """), {
            "sentiment": tweet["airline_sentiment"],
            "confidence": tweet["airline_sentiment_confidence"],
            "airline": tweet["airline"],
            "negativereason": tweet.get("negativereason"),
            "created_at": datetime.fromisoformat(tweet["tweet_created"]),
            "text": tweet["text"]
        })
        conn.commit()


def get_tweets(limit=100):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM tweets ORDER BY created_at DESC LIMIT :limit"),
            {"limit": limit}
        )

        tweets = []
        for row in result:
            tweets.append({
                "id": row[0],
                "sentiment": row[1],
                "confidence": row[2],
                "airline": row[3],
                "negativereason": row[4],
                "created_at": row[5],
                "text": row[6],
            })

        return tweets