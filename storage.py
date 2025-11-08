import json
import os
import datetime

DATA_FILE = "mood_data.json"

def save_entry(text, mood, reply):
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "text": text,
        "mood": mood,
        "reply": reply
    }
    data = []
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError):
            data = []
    data.append(entry)
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    except IOError as e:
        print(f"Error saving mood data: {e}")

def get_history():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []
