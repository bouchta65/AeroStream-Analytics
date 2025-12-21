import joblib
import os
from sentence_transformers import SentenceTransformer
import re
import string
import numpy as np


MODEL_PATH = "/app/models"

svm_model = joblib.load(MODEL_PATH + "/svm_model.pkl")

embedding_model = SentenceTransformer("BAAI/bge-large-en-v1.5")



def clean_text(text):
    text = text.lower()                       
    text = re.sub(r"http\S+|@\w+|#\w+", "", text)  
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.strip()


def predict_sentiment(texts):
    cleaned_texts = [clean_text(t) for t in texts]

    vectors = embedding_model.encode(cleaned_texts)

    predictions = svm_model.predict(vectors)

    probs = svm_model.predict_proba(vectors)

    results = []
    for i in range(len(texts)):
        results.append({
            "text": texts[i],
            "sentiment": predictions[i],
            "confidence": round(float(max(probs[i])), 3)
        })

    return results
