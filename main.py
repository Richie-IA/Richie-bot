from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Richie-IA est en ligne ✅ - Bot IA 24/7"

@app.route('/chat')
def chat():
    msg = request.args.get('message', '')
    if not msg:
        return jsonify({"error": "envoie ?message=ton_message"})
    
    # Réponse simple de ton IA
    reponse = f"Richie-IA a reçu: {msg}. Je suis en ligne et prêt à t'aider ! 🚀"
    return jsonify({
        "question": msg,
        "reponse": reponse,
        "status": "en ligne"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
