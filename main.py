from modules.voice_input import listen_command
from modules.voice_output import speak
from datetime import datetime
from modules.sentiment import detect_sentiment
from modules.emotion_detector import fake_emotion_classifier
from modules.personality import get_response
from modules.task_manager import add_task, remove_task, list_tasks
from modules.logger import log_interaction



EXIT_KEYWORDS = ["exit", "stop", "quit", "goodbye"]

if __name__ == "__main__":
    while True:
        command = listen_command()

        if command:
            print(f"User said: {command}")
            sentiment = detect_sentiment(command)

            if sentiment == "NEGATIVE":
                speak("You sound a bit down. Want to talk about it or maybe take a quick break?")
            elif sentiment == "POSITIVE":
                speak("Love the energy! Keep it going.")
            else:
                speak("Got it!")

            emotion = fake_emotion_classifier("user_voice.wav")
            print(f"🎭 Detected voice emotion: {emotion}")
            log_interaction(command, sentiment, emotion)

            if emotion == "Angry":
                speak("Take a breath. I'm here for you.")
            elif emotion == "Calm":
                speak("You sound chill. I like it.")

            # Pick personality style dynamically (optional logic)
            if sentiment == "NEGATIVE":
                style = "motivational"
            elif sentiment == "POSITIVE":
                style = "playful"
            else:
                style = "professional"

            # Get the assistant's styled reply
            reply = get_response(style)
            speak(reply)

            if "add task" in command:
                task = command.replace("add task", "").strip()
                message = add_task(task)
                speak(message)

            elif "remove task" in command:
                task = command.replace("remove task", "").strip()
                message = remove_task(task)
                speak(message)

            elif "show tasks" in command or "list tasks" in command:
                message = list_tasks()
                speak(message)

            if any(kw in command for kw in EXIT_KEYWORDS):
                speak("Goodbye! Have a productive day.")
                break

            elif "time" in command:
                current_time = datetime.now().strftime("%I:%M %p")
                speak(f"The current time is {current_time}")

            else:
                speak(f"You said: {command}")
