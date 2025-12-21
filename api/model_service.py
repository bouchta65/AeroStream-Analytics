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

