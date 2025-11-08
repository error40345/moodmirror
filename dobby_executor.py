import os
from openai import OpenAI

def load_persona():
    with open("prompts/dobby_persona.txt") as f:
        return f.read()

def generate_dobby_reply(user_text, mood):
    api_key = os.getenv("SENTIENT_API_KEY")
    
    if not api_key:
        return "Hi! I'd love to chat with you, but I need an API key to be set up first. Please add SENTIENT_API_KEY to your environment secrets."
    
    try:
        base_url = os.getenv("API_BASE_URL")
        
        if base_url:
            client = OpenAI(api_key=api_key, base_url=base_url)
        else:
            client = OpenAI(api_key=api_key)
        
        persona = load_persona()
        system_prompt = f"{persona}\nCurrent mood detected: {mood}\n"
        user_prompt = f"User said: {user_text}\nRespond empathetically, reflect mood, and give one small action."

        model = os.getenv("AI_MODEL", "accounts/sentientfoundation/models/dobby-unhinged-llama-3-3-70b-new")
        
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )

        return completion.choices[0].message.content
    except Exception as e:
        return f"I'm having trouble connecting right now. Error: {str(e)}"
