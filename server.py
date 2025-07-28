from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

def load_licenses():
    with open("licenses.json", "r") as f:
        return json.load(f)

@app.route("/check", methods=["POST"])
def check_license():
    licenses = load_licenses()
    data = request.get_json()
    key = data.get("key")

    if key not in licenses:
        return jsonify({"status": "error", "message": "Clé inconnue"}), 404

    expires = datetime.strptime(licenses[key]["expires"], "%Y-%m-%d")
    today = datetime.today()

    if today <= expires:
        return jsonify({"status": "ok", "message": "Licence valide"}), 200
    else:
        return jsonify({"status": "expired", "message": "Licence expirée"}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
