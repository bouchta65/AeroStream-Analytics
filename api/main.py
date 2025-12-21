from fastapi import FastAPI
from datetime import datetime, timezone
import random
from faker import Faker
from pipeline import process_tweets_pipeline
from database import init_db, get_tweets

app = FastAPI(title="Aerostream Analytics API")

@app.on_event("startup")
async def startup():
    init_db()

fake = Faker()
Faker.seed(42)

AIRLINES = ['Virgin America', 'United', 'Southwest', 'Delta', 'US Airways', 'American']

def generate_tweet() -> dict:
    airline = random.choice(AIRLINES)
    handle = {'Virgin America': '@VirginAmerica', 'United': '@united', 'Southwest': '@SouthwestAir', 
              'Delta': '@Delta', 'US Airways': '@USAirways', 'American': '@AmericanAir'}[airline]
    
    texts = [f"{handle} Great service!", f"{handle} flight delayed 4 hours!", f"{handle} flight was fine."]
    text = random.choice(texts)
    
    return {
        "airline": airline,
        "negativereason": None,
        "tweet_created": datetime.now(timezone.utc).isoformat(),
        "text": text
    }

@app.post("/batch")
def get_microbatch(batch_size: int = 10):
    batch_size = min(max(batch_size, 1), 100)
    tweets = [generate_tweet() for _ in range(batch_size)]
    return process_tweets_pipeline(tweets)


@app.get("/tweets")
def read_tweets(limit: int = 50):
    tweets = get_tweets(limit)
    return {
        "total": len(tweets),
        "tweets": tweets
    }