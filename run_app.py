import os
import subprocess

# Set AWS credentials directly in the environment
os.environ['AWS_ACCESS_KEY_ID'] = 'AKIASKYTDOW3WCIAZKJG'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'
os.environ['AWS_BUCKET_NAME'] = 'encryptedpasswords2'
os.environ['AWS_REGION'] = 'us-east-1'
os.environ['BRAKET_BUCKET_NAME'] = 'amazon-braket-results6'

# Print the environment variables for verification
print("AWS Configuration:")
print(f"Access Key ID: {os.environ.get('AWS_ACCESS_KEY_ID')}")
print(f"Bucket Name: {os.environ.get('AWS_BUCKET_NAME')}")
print(f"Region: {os.environ.get('AWS_REGION')}")

# Run the Flask application
subprocess.run(['python', 'app.py']) 