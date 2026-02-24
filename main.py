from emotion_model import detect_emotion
from voice import speak_text

def main():
    text = input("Enter your text: ")

    emotion = detect_emotion(text)
    print(f"Detected Emotion: {emotion}")

    speak_text(text, emotion)
    print("Audio generated as output.wav")

if __name__ == "__main__":
    main()