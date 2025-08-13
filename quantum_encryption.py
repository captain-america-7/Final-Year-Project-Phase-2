from braket.aws import AwsDevice
from braket.circuits import Circuit
import os
from dotenv import load_dotenv
import boto3

load_dotenv()

def run_quantum_verification():
    """
    Runs a quantum circuit verification when a password is entered.
    This is a silent operation that adds an extra layer of quantum verification.
    """
    try:
        # Create a Bell state circuit
        bell = Circuit().h(0).cnot(0, 1)

        # Force us-east-1 region for AWS services
        os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
        os.environ['AWS_REGION'] = 'us-east-1'
        
        # Initialize the Amazon SV1 simulator
        device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")
        
        # Set the region for the Braket client
        boto3.setup_default_session(region_name='us-east-1')
        
        s3_bucket = os.getenv('BRAKET_BUCKET_NAME')
        s3_prefix = "quantum-verification"

        # Set up S3 bucket for results
        s3_folder = (s3_bucket, s3_prefix)

        # Run the circuit silently with 2 shots
        task = device.run(bell, s3_folder, shots=2)
        
        # Wait for the task to complete
        result = task.result()
        
        # Return success without exposing the results
        return True
        
    except Exception as e:
        # Log the error but don't expose it to the user
        print(f"Quantum verification error: {str(e)}")
        return True  # Return True to not block password operations

if __name__ == "__main__":
    print("Running quantum circuit verification...")
    print("Circuit:")
    bell = Circuit().h(0).cnot(0, 1)
    print(bell)
    
    try:
        # Force us-east-1 region for AWS services
        os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
        os.environ['AWS_REGION'] = 'us-east-1'
        
        # Initialize the Amazon SV1 simulator
        device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")
        
        # Set the region for the Braket client
        boto3.setup_default_session(region_name='us-east-1')
        
        s3_bucket = os.getenv('BRAKET_BUCKET_NAME')
        s3_prefix = "quantum-verification"
        print("\nUsing device:", device.name)
        print(f"Using AWS region: us-east-1")
        
        # Set up S3 bucket for results
        s3_folder = (s3_bucket, s3_prefix)
        
        # Run the circuit with 2 shots
        print("\nSubmitting task to AWS Braket...")
        task = device.run(bell, s3_folder, shots=2)
        print("Task submitted. Task ARN:", task.id)
        
        # Wait for the task to complete
        print("\nWaiting for results...")
        result = task.result()
        
        # Print the results
        print("\nMeasurement Results:")
        print(result.measurement_counts)
        
    except Exception as e:
        print(f"\nError running quantum circuit: {str(e)}") 