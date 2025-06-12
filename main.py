from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow CORS from Netlify

@app.route("/location", methods=["POST"])
def receive_location():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    latitude = data.get("latitude")
    longitude = data.get("longitude")
    timestamp = data.get("timestamp")
    user_agent = data.get("userAgent")

    log_entry = f"[{timestamp}] Location: {latitude}, {longitude} | UA: {user_agent}\n"
    print(log_entry)

    # Optional: Save to file
    with open("locations.log", "a") as f:
        f.write(log_entry)

    return jsonify({"status": "Location received"}), 200

@app.route("/")
def home():
    return "Location Logger API is running!", 200
