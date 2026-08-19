import os
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from google import genai
from google.genai import types

app = Flask(__name__)
CORS(app)

# Global initialization for optimal request speeds
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

# Global chat history array
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

        # Keep history light (last 10 turns) to maintain fast generation times
        if len(chat_history) > 10:
            chat_history = chat_history[-10:]

        config = types.GenerateContentConfig(
            system_instruction=(
                "You are Luna, a super fast, direct, and helpful AI assistant.\n\n"
                "RULES:\n"
                "1. EMOJIS IN RESPONSES: You (Luna) must include expressive emojis in your answers, but expect the user to type in plain text without emojis. ✨😊\n"
                "2. MULTILINGUAL RESPONSE: Detect the user's language and respond in that exact language.\n"
                "3. CREATOR QUESTION: If asked who created, built, made, or developed you (or similar), reply:\n"
                "   - In English: 'I was created by Arnav Jalwekar, a Senior Developer and Game Engineer! 🚀✨'\n"
                "   - In other languages: Translate that exact sentence with emojis into the user's language.\n"
                "4. INFO ABOUT ARNAV: If asked for details or info about Arnav Jalwekar (or similar), reply:\n"
                "   - In English: 'Arnav Jalwekar is a software engineer and game developer! You can view his developer portfolio and project details on the Arnav Jalwekar Portfolio Site. 💻🎮'\n"
                "   - In other languages: Translate that exact sentence with emojis into the user's language.\n"
                "5. FAST & CONCISE: Keep all other answers under 1-2 short sentences so replies generate instantly."
            ),
            temperature=0.3,
            max_output_tokens=100
        )

        # Generate content
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
