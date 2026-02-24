from transformers import pipeline

emotion_classifier = pipeline(
    "text-classification",
    model="bhadresh-savani/distilbert-base-uncased-emotion"
)

def detect_emotion(text: str) -> str:
    result = emotion_classifier(text)[0]
    return result["label"]