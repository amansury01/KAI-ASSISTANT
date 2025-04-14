import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 175)    # Speaking speed
engine.setProperty('volume', 1.0)  # Max volume

def speak(text):
    print(f"🗣️ Assistant: {text}")
    engine.say(text)
    engine.runAndWait()
