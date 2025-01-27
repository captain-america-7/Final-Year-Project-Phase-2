from flask import Flask, request, jsonify, render_template
from braket.circuits import Circuit
from braket.devices import LocalSimulator
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__, template_folder="templates", static_folder="static")

# AWS Braket Local Simulator setup
device = LocalSimulator()

# In-memory storage for demonstration (use a database for production)
stored_passwords = {}

# Encrypt a password using a quantum circuit (Bell State)
def encrypt_password(password):
    try:
        circuit = Circuit().h(0).cnot(0, 1)  # Example quantum circuit
        result = device.run(circuit, shots=100).result().measurement_counts
        # Use the measurement counts as "encrypted" data (for simplicity in demo)
        return str(result)
    except Exception as e:
        raise ValueError(f"Error during encryption: {str(e)}")

# Decrypt the password (mock implementation since local simulation can't reverse it)
def decrypt_password(encrypted_data):
    try:
        # In this demo, return the encrypted data directly
        # Replace with decryption logic if applicable
        return f" {encrypted_data}"
    except Exception as e:
        raise ValueError(f"Error during decryption: {str(e)}")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_password():
    try:
        data = request.form
        service = data.get("service")
        username = data.get("username")
        password = data.get("password")

        if not service or not username or not password:
            return jsonify({"error": "Missing required fields."}), 400

        encrypted_data = encrypt_password(password)
        stored_passwords[service] = {
            "username": username,
            "password": password
        }

        return jsonify({"message": "Password added successfully."}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/retrieve", methods=["POST"])
def retrieve_password():
    try:
        data = request.form
        service = data.get("service")

        if not service:
            return jsonify({"error": "Service name is required."}), 400

        entry = stored_passwords.get(service)
        if not entry:
            return jsonify({"error": "Service not found."}), 404

        decrypted_password = decrypt_password(entry["password"])
        return jsonify({
            "service": service,
            "username": entry["username"],
            "password": decrypted_password
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/services", methods=["GET"])
def list_services():
    try:
        return jsonify({"services": list(stored_passwords.keys())}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
