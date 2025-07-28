import streamlit as st
import whisper
from transformers import pipeline
import datetime
import os

# Load models
voice_to_text_model = whisper.load_model("base")
emotion_classifier = pipeline("text-classification", 
                              model="j-hartmann/emotion-english-distilroberta-base", 
                              top_k=None)


def voice_to_text(audio_path):
    text = voice_to_text_model.transcribe(audio_path)
    return text["text"].strip()

def sentiment_analysis(text, top_k=2):
    emotions = emotion_classifier(text)[0]
    top_emotions = sorted(emotions, key=lambda x: x['score'], reverse=True)[:top_k]
    return [(emo['label'], round(emo['score'], 3)) for emo in top_emotions]

def save_journal_entry(text, emotions):
    return {
        "Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Text": text,
        "Emotions": emotions
    }

# Streamlit UI
st.title("🎙️ Voice-to-Text Travel Journal with Emotion Detection")

audio_path = None

uploaded_file = st.file_uploader("Upload your audio file (MP3/WAV)", type=["mp3", "wav"])

if uploaded_file is not None:
    audio_path = "uploaded_audio.wav"
    with open(audio_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success("Audio uploaded successfully!")

if audio_path:
    text = voice_to_text(audio_path)
    st.subheader("Transcribed Text")
    st.write(text)

    emotions = sentiment_analysis(text)
    formatted_emotions = ", ".join([f"{label} ({score})" for label, score in emotions])
    st.write(f"Detected Emotions: {formatted_emotions}")


    save_journal_entry(text, emotions)

    if os.path.exists(audio_path):
        os.remove(audio_path)