import requests
import os

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

def predict_fake_news(text):
    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": text}
    )

    result = response.json()[0]

    label = result["label"]
    score = result["score"] * 100

    if label == "NEGATIVE":
        return {
            "label": "FAKE",
            "fake_probability": round(score, 2),
            "real_probability": round(100 - score, 2)
        }
    else:
        return {
            "label": "REAL",
            "fake_probability": round(100 - score, 2),
            "real_probability": round(score, 2)
        }
