from sentiment_toolkit import analyze_emotion
from dobby_executor import generate_dobby_reply
from storage import save_entry
from roma_executor import create_roma_executor

roma_executor = create_roma_executor()

def process_message(text):
    if not text or not text.strip():
        return "I'm here to listen. How are you feeling today?"
    
    mood = analyze_emotion(text)
    
    if roma_executor and roma_executor.is_complex_task(text):
        try:
            reply = roma_executor.execute(text, mood)
            save_entry(text, mood, f"[ROMA] {reply}")
        except Exception as e:
            print(f"ROMA failed, falling back to Sentient: {e}")
            reply = generate_dobby_reply(text, mood)
            save_entry(text, mood, f"[Sentient-Fallback] {reply}")
    else:
        reply = generate_dobby_reply(text, mood)
        save_entry(text, mood, f"[Sentient] {reply}")
    
    return reply
