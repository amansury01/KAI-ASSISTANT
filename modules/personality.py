import random

PERSONALITY_MODES = {
    "motivational": [
        "You're stronger than you think.",
        "Keep pushing. You’re almost there!",
        "Focus. You’ve got this!"
    ],
    "playful": [
        "Look at you go! Crushing it 🐱‍🏍",
        "Haha, okay genius, let’s keep going 😎",
        "You're hilarious... now focus up!"
    ],
    "taunting": [
        "Oh look, procrastination again? Classic.",
        "You sure you're working or just chilling again?",
        "If laziness was a skill, you'd be a legend."
    ],
    "professional": [
        "Task received. Proceeding with precision.",
        "Acknowledged. What's next?",
        "Ready for your next directive."
    ]
}

# default: personality based on sentiment
user_selected_mode = None

def set_mode(mode):
    global user_selected_mode
    if mode in PERSONALITY_MODES:
        user_selected_mode = mode
        return f"Personality set to {mode} mode."
    else:
        return "Unknown personality mode."

def get_response(style):
    mode = user_selected_mode if user_selected_mode else style
    return random.choice(PERSONALITY_MODES.get(mode, ["Let's keep going."]))
