from fastapi import FastAPI
from pydantic import BaseModel
from model.fake_news_model import predict_fake_news
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Fake News Detection API")

# ✅ CORS (VERY IMPORTANT for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later you can restrict this
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
        "news_preview": news.text[:60],
        "label": result["label"],
        "fake_probability": result["fake_probability"],
        "real_probability": result["real_probability"]
    }
