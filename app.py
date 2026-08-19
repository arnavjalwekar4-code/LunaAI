import os
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from google import genai
from google.genai import types

app = Flask(__name__)
CORS(app)

# Pull API Key safely from environment variable
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

# Global chat history array to remember conversations
chat_history = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global chat_history
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()
        
        if not user_message:
            return jsonify({"success": False, "error": "Empty message"})

        # Append user message to history
        chat_history.append({"role": "user", "parts": [{"text": user_message}]})

        config = types.GenerateContentConfig(
            system_instruction=(
                "You are Luna, an intelligent and accurate AI assistant. "
                "Only mention that you were created by Arnav Jalwekar if the user specifically asks who created, built, made, or developed you. "
                "For all other questions, answer directly and accurately in 1-2 short sentences without bringing up your creator or introducing yourself. "
                "Maintain conversational memory using the chat context provided."
            ),
            temperature=0.2
        )

        # Pass full conversation history
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=chat_history,
            config=config
        )

        reply_text = response.text.strip()
        
        # Append assistant response to history
        chat_history.append({"role": "model", "parts": [{"text": reply_text}]})

        return jsonify({"success": True, "reply": reply_text})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/reset', methods=['POST'])
def reset():
    global chat_history
    chat_history = []
    return jsonify({"success": True})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
