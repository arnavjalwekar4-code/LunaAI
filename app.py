import os
from flask import Flask, render_template, request, jsonify, session
import google.generativeai as genai

app = Flask(__name__)
# Secret key required for managing user chat sessions
app.secret_key = os.environ.get("FLASK_SECRET_KEY", os.urandom(24))

# Configure Gemini API
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    # Uses Gemini Flash for ultra-fast response generation
    model = genai.GenerativeModel("gemini-2.5-flash")
else:
    model = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    if not model:
        return jsonify({
            "success": False,
            "reply": "Gemini API key missing. Please set GEMINI_API_KEY environment variable."
        }), 500

    data = request.get_json() or {}
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"success": False, "reply": "Please enter a valid message."}), 400

    try:
        # Retrieve active chat session history
        history = session.get("history", [])

        # Start Gemini chat with history context
        chat_session = model.start_chat(history=history)
        response = chat_session.send_message(user_message)

        # Update and save chat history back to flask session
        updated_history = []
        for msg in chat_session.history:
            updated_history.append({
                "role": msg.role,
                "parts": [part.text for part in msg.parts]
            })
        session["history"] = updated_history

        return jsonify({
            "success": True,
            "reply": response.text
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "reply": f"An error occurred: {str(e)}"
        }), 500

@app.route("/reset", methods=["POST"])
def reset():
    session.pop("history", None)
    return jsonify({"success": True, "message": "Conversation history cleared."})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
