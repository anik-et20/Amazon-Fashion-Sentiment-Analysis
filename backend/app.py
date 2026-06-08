from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("sentiment_model.pkl")
tfidf = joblib.load("tfidf.pkl")


class Review(BaseModel):
    review: str


@app.get("/")
def home():
    return {"message": "Amazon Sentiment API Running"}


@app.post("/predict")
def predict(data: Review):

    review_vector = tfidf.transform([data.review])

    prediction = model.predict(review_vector)[0]

    probabilities = model.predict_proba(review_vector)[0]

    return {
        "sentiment": prediction,
        "confidence": float(max(probabilities))
    }