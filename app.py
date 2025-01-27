from flask import Flask, request, jsonify, render_template
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.fernet import Fernet
from braket.circuits import Circuit
from braket.devices import LocalSimulator
import boto3
import os
from dotenv import load_dotenv
import json
import random


# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__, template_folder="templates", static_folder="static")

# AWS Braket Local Simulator setup
device = LocalSimulator()


# Generate RSA key pair (for encryption)
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
public_key = private_key.public_key()

# Serialize keys (for optional storage or export)
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption(),
).decode()

public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
).decode()

# AWS S3 setup
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION"),
)
bucket_name = os.getenv("S3_BUCKET_NAME")  # Set your bucket name in .env

encryption_key = os.getenv("ENCRYPTION_KEY") or Fernet.generate_key()
cipher = Fernet(encryption_key)


# Quantum Key Distribution (QKD) using BB84
def qkd_generate_key(length=10):
    try:
        # Generate random basis and bit choices for Alice
        alice_bases = [random.choice(["X", "Z"]) for _ in range(length)]
        alice_bits = [random.randint(0, 1) for _ in range(length)]

        # Create quantum circuit
        circuit = Circuit()
        for i in range(length):
            if alice_bits[i] == 1:
                circuit.x(i)  # Apply X gate if bit is 1
            if alice_bases[i] == "X":
                circuit.h(i)  # Apply H gate for "X" basis

        # Simulate the quantum circuit
        results = device.run(circuit, shots=1).result().measurement_counts
        measured_bits = list(results.keys())[0]

        # Bob's random basis choices
        bob_bases = [random.choice(["X", "Z"]) for _ in range(length)]

        # Key reconciliation: Keep only bits where bases match
        final_key = []
        for i in range(length):
            if alice_bases[i] == bob_bases[i]:
                final_key.append(int(measured_bits[i]))

        return final_key
    except Exception as e:
        raise ValueError(f"Error during QKD: {str(e)}")


# Encrypt a password using a quantum circuit (Bell State)
def encrypt_password(password):
    try:
        circuit = Circuit().h(0).cnot(0, 1)
        result = device.run(circuit, shots=100).result().measurement_counts
        return cipher.encrypt(password.encode()).decode()
    except Exception as e:
        raise ValueError(f"Error during encryption: {str(e)}")

# Encrypt a password using RSA
def rsa(password):
    try:
        encrypted = public_key.encrypt(
            password.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
        return encrypted.hex() 
    except Exception as e:
        raise ValueError(f"Error during encryption: {str(e)}")

# Decrypt the password
def decrypt_password(encrypted_data):
    try:
        
        return cipher.decrypt(encrypted_data.encode()).decode()
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
        s3_key = f"passwords/{service}.json"
        s3_object = {
            "username": username,
            "encrypted_password": encrypted_data,
        }

        # Store the password in S3
        s3.put_object(
            Bucket=bucket_name,
            Key=s3_key,
            Body=json.dumps(s3_object),
            ContentType="application/json",
        )

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

        s3_key = f"passwords/{service}.json"

        # Retrieve the password from S3
        try:
            response = s3.get_object(Bucket=bucket_name, Key=s3_key)
            stored_data = json.loads(response["Body"].read())
        except s3.exceptions.NoSuchKey:
            return jsonify({"error": "Service not found."}), 404

        decrypted_password = decrypt_password(stored_data["encrypted_password"])
        return jsonify({
            "service": service,
            "username": stored_data["username"],
            "password": decrypted_password,
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/services", methods=["GET"])
def list_services():
    try:
        # List all services stored in S3
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix="passwords/")
        services = [
            obj["Key"].split("/")[-1].split(".json")[0]
            for obj in response.get("Contents", [])
        ]
        return jsonify({"services": services}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
