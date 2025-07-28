# 🎙️ Voice-to-Text Travel Journal with Emotion Detection

This project is a simple yet powerful **Streamlit web app** that allows users to upload an audio file describing their travel experience. The app transcribes the audio using OpenAI's **Whisper** model and detects the top emotional tones using a **transformers-based emotion classification model**.

---

## 🚀 Features

- ✅ Upload MP3 or WAV audio files  
- ✅ Transcribes speech to text using Whisper  
- ✅ Detects top 2 emotions using a DistilRoBERTa emotion classifier  
- ✅ Displays clean, readable transcriptions  
- ✅ Summarizes emotions alongside the journal entry  
- ✅ Deletes temporary audio files for security

---

## 🔧 Tech Stack

| Component         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `Streamlit`      | Frontend web app framework                                                  |
| `Whisper`        | OpenAI’s speech recognition model for audio transcription                  |
| `Transformers`   | 🤗 HuggingFace model (`j-hartmann/emotion-english-distilroberta-base`) for emotion analysis |
| `Python`         | Core programming language                                                   |

---

## 📦 Installation

Make sure Python 3.8 or above is installed. Then follow the steps below:

```bash
# Clone this repository
git clone https://github.com/Mani-Rmk/Voice-to-Text-Travel-Journal-with-Emotion-Detection.git
cd Voice-to-Text-Travel-Journal-with-Emotion-Detection

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
