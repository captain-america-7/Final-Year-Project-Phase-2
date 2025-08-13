import os
import subprocess

# Set AWS credentials directly in the environment
# Replace with your actual AWS credentials
os.environ['AWS_ACCESS_KEY_ID'] = 'YOUR_AWS_ACCESS_KEY_ID_HERE'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'YOUR_AWS_SECRET_ACCESS_KEY_HERE'
os.environ['AWS_BUCKET_NAME'] = 'YOUR_S3_BUCKET_NAME_HERE'
os.environ['AWS_REGION'] = 'us-east-1'
os.environ['BRAKET_BUCKET_NAME'] = 'YOUR_BRAKET_BUCKET_NAME_HERE'

# Print the environment variables for verification
print("AWS Configuration:")
print(f"Access Key ID: {os.environ.get('AWS_ACCESS_KEY_ID')}")
print(f"Bucket Name: {os.environ.get('AWS_BUCKET_NAME')}")
print(f"Region: {os.environ.get('AWS_REGION')}")

# Run the Flask application
subprocess.run(['python', 'app.py']) 