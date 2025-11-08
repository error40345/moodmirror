import re

EMOTION_KEYWORDS = {
    "joy": ["happy", "joyful", "excited", "amazing", "wonderful", "great", "love", "fantastic", "excellent", "glad", "delighted", "cheerful"],
    "sadness": ["sad", "unhappy", "depressed", "down", "miserable", "heartbroken", "crying", "tears", "grief", "sorrow"],
    "anger": ["angry", "mad", "furious", "annoyed", "frustrated", "irritated", "rage", "hate", "bitter"],
    "fear": ["scared", "afraid", "anxious", "worried", "nervous", "panic", "terrified", "fearful", "frightened"],
    "surprise": ["surprised", "shocked", "amazed", "astonished", "unexpected", "sudden"],
    "neutral": ["okay", "fine", "alright", "normal", "regular"],
    "tired": ["tired", "exhausted", "drained", "weary", "fatigued", "sleepy"],
    "stressed": ["stressed", "overwhelmed", "pressure", "tense", "strained"]
}

def analyze_emotion(text):
    text_lower = text.lower()
    emotion_scores = {}
    
    for emotion, keywords in EMOTION_KEYWORDS.items():
        score = 0
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', text_lower):
                score += 1
        if score > 0:
            emotion_scores[emotion] = score
    
    if not emotion_scores:
        return "neutral (0.50)"
    
    detected_emotion = max(emotion_scores.keys(), key=lambda e: emotion_scores[e])
    confidence = min(0.95, 0.60 + (emotion_scores[detected_emotion] * 0.15))
    
    return f"{detected_emotion} ({confidence:.2f})"
