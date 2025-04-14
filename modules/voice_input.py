import speech_recognition as sr

def listen_command():
    print("🔍 Entered listen_command()")
    recognizer = sr.Recognizer()

    # Check available mics
    mic_list = sr.Microphone.list_microphone_names()
    for i, mic in enumerate(mic_list):
        print(f"[{i}] {mic}")

    # Choose the appropriate mic index here
    with sr.Microphone(device_index=0) as source:  # Try changing index if needed
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # helps with background noise
        audio = recognizer.listen(source)
        with open("user_voice.wav", "wb") as f:
            f.write(audio.get_wav_data())
        try:
            print("🧠 Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"✅ You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("❌ Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            print("🚫 Could not reach Google Speech API.")
            return None
