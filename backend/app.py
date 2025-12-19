from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model.fake_news_model import predict_fake_news

app = FastAPI(title="Fake News Detection API")

# ✅ CORS CONFIG (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://projecthub-1vto.onrender.com",  # your frontend URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class News(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Fake News Detection API is running"}

@app.post("/predict")
def predict(news: News):
    result = predict_fake_news(news.text)
    return {
        "label": result["label"],
        "fake_probability": result["fake_probability"],
        "real_probability": result["real_probability"],
    }
