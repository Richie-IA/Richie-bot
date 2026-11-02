from flask import Flask, request, jsonify

app = Flask(__name__)

def reponse_ia(message):
    message = message.lower()
    if "salut" in message or "bonjour" in message:
        return "Salut ! Moi c'est Richie-IA 🤖 Comment je peux t'aider ?"
    elif "qui es tu" in message:
        return "Je suis Richie-IA, une intelligence artificielle cree par Richie"
    else:
        return f"Tu as dit : '{message}'. Pose-moi une autre question !"

@app.route('/')
def home():
    return "<h1>Richie-IA est en ligne ✅</h1><p>Test : /chat?message=salut</p>"

@app.route('/chat')
def chat():
    msg = request.args.get('message', '')
    return jsonify({"question": msg, "reponse": reponse_ia(msg)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
