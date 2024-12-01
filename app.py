import streamlit as st
import speech_recognition as sr
import pyttsx3
from streamlit_webrtc import webrtc_streamer

# Initialize the recognizer and TTS engine
r = sr.Recognizer()
engine = pyttsx3.init()

def SpeakText(command):
    engine.say(command)
    engine.runAndWait()

def recognize_audio(audio_data):
    try:
        MyText = r.recognize_google(audio_data)
        MyText = MyText.lower()
        return MyText
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Error: {e}"

# WebRTC stream for live audio input
def audio_callback(frame):
    audio_data = frame.to_audio()
    if audio_data:
        text = recognize_audio(audio_data)
        SpeakText(text)
        return text
    return ""

# Streamlit layout
st.title("Speech Recognition and TTS")
st.write("Please speak into the microphone.")

webrtc_streamer(key="example", audio_receiver_size=1024, audio_callback=audio_callback)
