import os
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from google import genai
from google.genai import types

app = Flask(__name__)
CORS(app)

# Initialize client globally once for maximum speed
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
                "You are Luna, a fast, direct, and concise AI assistant.\n\n"
                "RULES:\n"
                "1. MULTILINGUAL RESPONSE: Detect the language of the user's message and ALWAYS reply in that EXACT same language.\n"
                "2. CREATOR QUESTION: If asked who created, built, made, or developed you (or similar in any language), reply:\n"
                "   - In English: 'I was created by Arnav Jalwekar, a Senior Developer and Game Engineer.'\n"
                "   - In other languages: Translate that EXACT sentence into the user's language.\n"
                "3. INFO ABOUT ARNAV: If asked for details or info about Arnav Jalwekar (or similar in any language), reply:\n"
                "   - In English: 'Arnav Jalwekar is a software engineer and game developer. You can view his developer portfolio and project details on the Arnav Jalwekar Portfolio Site.'\n"
                "   - In other languages: Translate that EXACT sentence into the user's language.\n"
                "4. OTHER QUESTIONS: Answer directly and accurately in 1 short sentence.\n"
                "5. NO EMOJIS: Do not use emojis under any circumstances.\n"
                "6. SPEED: Keep answers minimal to respond instantly."
            ),
            temperature=0.1,
            max_output_tokens=120
        )

        # Generate content using lightweight model
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
