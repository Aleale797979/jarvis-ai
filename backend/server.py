import os

from flask import Flask, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# La chiave NON viene scritta nel codice.
# Verrà inserita nelle variabili d'ambiente di Render.
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if OPENAI_API_KEY:
    client = OpenAI(api_key=OPENAI_API_KEY)
else:
    client = None


@app.route("/")
def home():
    return jsonify({
        "service": "JARVIS",
        "status": "online"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "openai_configured": client is not None
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
