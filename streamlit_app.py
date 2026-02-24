import streamlit as st
from emotion_model import detect_emotion
from voice import speak_text, EMOTION_VOICE_MAP
import os

st.set_page_config(page_title="Empathy Engine", page_icon="🎙️")

st.title("🎙️ Empathy Engine")
st.write("Enter text and generate emotionally expressive speech.")

text = st.text_area("Enter your text here:")

if st.button("Generate Emotional Voice"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing emotion and generating voice..."):

            emotion = detect_emotion(text)

            settings = EMOTION_VOICE_MAP.get(
                emotion,
                EMOTION_VOICE_MAP["neutral"]
            )

            audio_path = speak_text(text, emotion)

        st.success(f"Detected Emotion: {emotion}")

        st.subheader("Applied Voice Parameters")
        st.info(f"Rate Applied: {settings['rate']}")
        st.info(f"Volume Applied: {settings['volume']}")
        st.info(f"Pitch Shift Applied: {settings['pitch_shift']}")

        if os.path.exists(audio_path):
            st.audio(audio_path)


st.markdown("---")
st.subheader("Emotion to Voice Mapping")

st.table(EMOTION_VOICE_MAP)