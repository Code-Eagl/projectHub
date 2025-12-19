#
# from transformers import pipeline
#
# classifier = pipeline(
#     "sentiment-analysis",
#     model="distilbert-base-uncased-finetuned-sst-2-english"
# )
#
# def predict_fake_news(text):
#     result = classifier(text)[0]
#
#     score = round(result["score"] * 100, 2)
#
#     if result["label"] == "NEGATIVE":
#         return {
#             "label": "FAKE",
#             "fake_probability": score,
#             "real_probability": round(100 - score, 2)
#         }
#     else:
#         return {
#             "label": "REAL",
#             "fake_probability": round(100 - score, 2),
#             "real_probability": score
#         }
# backend/model/fake_news_model.py
from transformers import pipeline

# Load the sentiment-analysis pipeline (DistilBERT fine-tuned)
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def predict_fake_news(text: str):
    """
    Predict whether a news article is REAL or FAKE.
    Returns a dictionary with label, fake_probability, real_probability
    """
    # Run classification
    result = classifier(text[:512])[0]  # Limit text to first 512 tokens

    # Hugging Face output: {'label': 'POSITIVE', 'score': 0.98} etc.
    # Map POSITIVE -> REAL, NEGATIVE -> FAKE
    if result["label"].upper() == "POSITIVE":
        label = "REAL"
        real_probability = result["score"] * 100
        fake_probability = 100 - real_probability
    else:
        label = "FAKE"
        fake_probability = result["score"] * 100
        real_probability = 100 - fake_probability

    return {
        "label": label,
        "real_probability": round(real_probability, 2),
        "fake_probability": round(fake_probability, 2)
    }

# Optional: quick test
if __name__ == "__main__":
    test_text_real = "Breaking news! Government announces new education policy."
    test_text_fake = "Aliens have landed in New York City!"
    print(predict_fake_news(test_text_real))
    print(predict_fake_news(test_text_fake))
