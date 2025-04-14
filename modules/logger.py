import json
import os
from datetime import datetime

LOG_FILE = "data/mood_log.json"

def log_interaction(text, sentiment, emotion):
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "text": text,
        "sentiment": sentiment,
        "emotion": emotion
    }

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([log_entry], f, indent=2)
    else:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
        logs.append(log_entry)
        with open(LOG_FILE, "w") as f:
            json.dump(logs, f, indent=2)
