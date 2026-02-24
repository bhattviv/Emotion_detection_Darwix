import pyttsx3
import os
from datetime import datetime

os.makedirs("static", exist_ok=True)

EMOTION_VOICE_MAP = {
    "joy": {
        "rate": 220,
        "volume": 1.0,
        "pitch_shift": 20
    },
    "love": {
        "rate": 200,
        "volume": 1.0,
        "pitch_shift": 10
    },
    "anger": {
        "rate": 210,
        "volume": 1.2,
        "pitch_shift": -10
    },
    "sadness": {
        "rate": 130,
        "volume": 0.7,
        "pitch_shift": -20
    },
    "fear": {
        "rate": 150,
        "volume": 0.8,
        "pitch_shift": -5
    },
    "surprise": {
        "rate": 230,
        "volume": 1.1,
        "pitch_shift": 25
    },
    "neutral": {
        "rate": 170,
        "volume": 1.0,
        "pitch_shift": 0
    }
}


def speak_text(text, emotion):
    engine = pyttsx3.init()

    settings = EMOTION_VOICE_MAP.get(
        emotion,
        EMOTION_VOICE_MAP["neutral"]
    )

    adjusted_rate = settings["rate"] + settings["pitch_shift"]
    engine.setProperty("rate", adjusted_rate)

    engine.setProperty("volume", min(settings["volume"], 1.0))

    emotion_folder = os.path.join("static", emotion)
    os.makedirs(emotion_folder, exist_ok=True)

    filename = f"{emotion}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
    output_path = os.path.join(emotion_folder, filename)

    engine.save_to_file(text, output_path)
    engine.runAndWait()

    return output_path