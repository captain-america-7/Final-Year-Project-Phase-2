from braket.aws import AwsDevice
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def list_available_devices():
    """
    Lists all available quantum devices on AWS Braket.
    """
    # Set the region for the Braket client
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
    os.environ['AWS_REGION'] = 'us-east-1'
    boto3.setup_default_session(region_name='us-east-1')
    
    print("Listing available quantum devices on AWS Braket...")
    print("Region: us-east-1")
    print("\n")
    
    # Get all devices
    devices = AwsDevice.get_devices()
    
    # Filter for available devices
    available_devices = [device for device in devices if device.status == 'ONLINE']
    
    if not available_devices:
        print("No available devices found.")
        return
    
    print(f"Found {len(available_devices)} available devices:")
    print("\n")
    
    for i, device in enumerate(available_devices, 1):
        print(f"Device {i}:")
        print(f"  Name: {device.name}")
        print(f"  ARN: {device.arn}")
        print(f"  Provider: {device.provider_name}")
        print(f"  Type: {device.type}")
        print(f"  Status: {device.status}")
        print("\n")

if __name__ == "__main__":
    list_available_devices() 