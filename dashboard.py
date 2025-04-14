import streamlit as st
import json
import os

st.set_page_config(page_title="KAII Dashboard", layout="centered")

st.title("📊 KAII Assistant Dashboard")
st.markdown("View your mood trends, assistant logs, and task list.")

# Load interaction logs
def load_logs():
    if os.path.exists("data/interaction_log.json"):
        with open("data/interaction_log.json", "r") as f:
            return json.load(f)
    return []

logs = load_logs()

if logs:
    st.subheader("🧠 Recent Interactions")

    for entry in logs[-5:][::-1]:  # Show last 5 logs
        st.write(f"**You said:** {entry['command']}")
        st.write(f"Sentiment: `{entry['sentiment']}` | Emotion: `{entry['emotion']}`")
        st.markdown("---")
else:
    st.info("No interaction logs yet.")

# Current mode
st.subheader("🎭 Assistant Mode")
mode_file = "data/mode.txt"
if os.path.exists(mode_file):
    with open(mode_file, "r") as f:
        mode = f.read().strip()
        st.write(f"Current mode: `{mode}`")
else:
    st.write("No mode set.")
