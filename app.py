from gtts import gTTS
import speech_recognition as sr
import streamlit as st

# Function to convert text to speech
def SpeakText(command):
    tts = gTTS(text=command, lang='en')
    tts.save("output.mp3")
    st.audio("output.mp3", format="audio/mp3")

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

            MyText = r.recognize_google(audio)
            MyText = MyText.lower()

            st.write(f"Did you say: {MyText}")
            SpeakText(MyText)

    except sr.UnknownValueError:
        st.write("Sorry, I did not catch that.")
    except sr.RequestError as e:
        st.write(f"Could not request results; {e}")
