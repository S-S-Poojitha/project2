import streamlit as st
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import io
import wave
import pyaudio
from gtts import gTTS

# Function to convert text to speech
def speak_text(command):
    tts = gTTS(text=command, lang='en')
    tts.save("output.mp3")
    st.audio("output.mp3", format="audio/mp3")

# Function for speech recognition with Google Cloud Speech-to-Text
def recognize_speech():
    client = speech.SpeechClient()

    # Read the audio file
    audio_file = "path_to_your_audio_file.wav"  # Add path to your audio file
    with io.open(audio_file, "rb") as audio:
        content = audio.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)
    for result in response.results:
        return result.alternatives[0].transcript

# Streamlit UI
st.title("Speech Recognition with Google Cloud API")
if st.button("Start Listening"):
    speech = recognize_speech()
    st.write(f"Recognized Speech: {speech}")
    speak_text(speech)
