from database import engine, text


def get_tweets_by_ccompagnie():
    with engine.connect() as conn:
        rows = conn.execute(text("""
            SELECT airline, COUNT(*) FROM tweets
            GROUP BY airline
        """)).fetchall()
    return [dict(zip(['airline', 'count'], row)) for row in rows]


def get_sentiment_by_companie():
    with engine.connect() as conn:
        rows = conn.execute(text("""
            SELECT airline, sentiment, COUNT(*) 
            FROM tweets 
            GROUP BY airline, sentiment
        """)).fetchall()
    return [dict(zip(['airline', 'sentiment', 'count'], row)) for row in rows]


def get_pourcentage_satisfaction():
    with engine.connect() as conn:
        rows = conn.execute(text("""
            SELECT airline, 
                   ROUND(100.0 * SUM(CASE sentiment WHEN 'positive' THEN 1 ELSE 0 END) / COUNT(*), 2) as prc_sent
            FROM tweets 
            GROUP BY airline
        """)).fetchall()
    return [dict(zip(['airline', 'satisfaction_pct'], row)) for row in rows]


def get_reason_negative():
    with engine.connect() as conn:
        rows = conn.execute(text("""
            SELECT negativereason, COUNT(negativereason) 
            FROM tweets 
            WHERE sentiment = 'negative' 
            GROUP BY negativereason
            ORDER BY COUNT(negativereason) DESC
        """)).fetchall()
    return [dict(zip(['reason', 'count'], row)) for row in rows]


def get_count_tweets():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM tweets")).fetchone()
    return result[0] if result else 0


def get_count_companie():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(DISTINCT airline) FROM tweets")).fetchone()
    return result[0] if result else 0


def pourcentage_negative_tweets():
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT ROUND(100.0 * SUM(CASE sentiment WHEN 'negative' THEN 1 ELSE 0 END) / 
                   NULLIF(COUNT(*), 0), 2) 
            FROM tweets
        """)).fetchone()
    return result[0] if result and result[0] is not None else 0

