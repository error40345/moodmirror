from flask import Flask, request, jsonify, render_template
from roma_pipeline import process_message
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SESSION_SECRET', 'dev-secret-key-change-in-production')

@app.after_request
def add_no_cache_headers(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    user_text = data.get("text", "")
    reply = process_message(user_text)
    
    from sentiment_toolkit import analyze_emotion
    mood = analyze_emotion(user_text) if user_text else None
    
    return jsonify({"reply": reply, "mood": mood})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
