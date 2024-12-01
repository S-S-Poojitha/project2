import streamlit as st
import pyttsx3
import speech_recognition as sr

# Initialize the recognizer and TTS engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak the text
def SpeakText(command):
    engine.say(command)
    engine.runAndWait()

# Streamlit UI components
st.title("Speech Recognition and Text-to-Speech App")
st.write("Speak something and I will repeat it.")

# Button to start listening
if st.button("Start Listening"):
    with st.spinner("Listening..."):
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
                audio = r.listen(source)  # Capture the audio
                st.write("Recognizing...")
                MyText = r.recognize_google(audio)  # Recognize speech using Google API
                MyText = MyText.lower()
                st.write(f"Did you say: {MyText}")
                SpeakText(MyText)  # Speak the recognized text
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand your speech.")
        except sr.RequestError as e:
            st.error(f"Could not request results; {e}")
