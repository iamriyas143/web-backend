from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

@app.route("/location", methods=["POST"])
def receive_location():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    latitude = data.get("latitude")
    longitude = data.get("longitude")
    timestamp = data.get("timestamp")
    user_agent = data.get("userAgent")

    # Extract real IP (handle proxy)
    ip_address = request.headers.get("X-Forwarded-For", request.remote_addr)

    log_entry = (
        f"[{timestamp}] IP: {ip_address} | Location: {latitude}, {longitude} | "
        f"UA: {user_agent}\n"
    )

    print(log_entry)

    # Save to file
    with open("locations.log", "a") as f:
        f.write(log_entry)

    return jsonify({"status": "Location and IP received"}), 200

@app.route("/")
def home():
    return "Location Logger API is running!", 200
