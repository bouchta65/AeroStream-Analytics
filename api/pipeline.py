from model_service import predict_sentiment
from database import save_tweet
from datetime import datetime


def process_tweets_pipeline(tweets):
    texts = []
    for tweet in tweets:
        texts.append(tweet.get("text", ""))

    results = predict_sentiment(texts)

    for tweet, result in zip(tweets, results):
        save_tweet({
            "airline_sentiment": result["sentiment"],
            "airline_sentiment_confidence": result["confidence"],
            "airline": tweet.get("airline", "Unknown"),
            "negativereason": tweet.get("negativereason"),
            "tweet_created": tweet.get(
                "tweet_created",
                datetime.now().isoformat()
            ),
            "text": tweet.get("text")
        })

    return {
        "status": "success",
        "processed": len(tweets)
    }


