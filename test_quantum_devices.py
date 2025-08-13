from braket.aws import AwsDevice
from braket.circuits import Circuit
import os
from dotenv import load_dotenv
import boto3
import time
from datetime import datetime

# Load environment variables
load_dotenv()

def list_all_devices():
    """
    Lists all quantum devices available on AWS Braket.
    """
    print("Listing all quantum devices on AWS Braket...")
    print("=" * 80)
    
    # Get all devices
    devices = AwsDevice.get_devices()
    
    if not devices:
        print("No devices found.")
        return []
    
    print(f"Found {len(devices)} devices:")
    print("-" * 80)
    
    for i, device in enumerate(devices, 1):
        print(f"Device {i}:")
        print(f"  Name: {device.name}")
        print(f"  ARN: {device.arn}")
        print(f"  Provider: {device.provider_name}")
        print(f"  Type: {device.type}")
        print(f"  Status: {device.status}")
        print(f"  Region: {device.arn.split(':')[3]}")
        print("-" * 80)
    
    return devices

def test_device(device, shots=2):
    """
    Tests a quantum device by running a simple Bell state circuit.
    """
    print(f"\nTesting device: {device.name}")
    print(f"ARN: {device.arn}")
    print(f"Status: {device.status}")
    
    if device.status != 'ONLINE':
        print(f"Device is not ONLINE. Current status: {device.status}")
        return False
    
    try:
        # Create a Bell state circuit
        bell = Circuit().h(0).cnot(0, 1)
        print("\nCircuit:")
        print(bell)
        
        # Get the region from the device ARN
        region = device.arn.split(':')[3]
        
        # Set the region for the Braket client
        os.environ['AWS_DEFAULT_REGION'] = region
        os.environ['AWS_REGION'] = region
        boto3.setup_default_session(region_name=region)
        
        # Set up S3 bucket for results
        s3_bucket = os.getenv('BRAKET_BUCKET_NAME')
        s3_prefix = f"test-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        s3_folder = (s3_bucket, s3_prefix)
        
        # Run the circuit
        print(f"\nSubmitting task to AWS Braket in region {region}...")
        task = device.run(bell, s3_folder, shots=shots)
        print(f"Task submitted. Task ARN: {task.id}")
        
        # Wait for the task to complete
        print("Waiting for results...")
        result = task.result()
        
        # Print the results
        print("\nMeasurement Results:")
        print(result.measurement_counts)
        
        return True
        
    except Exception as e:
        print(f"Error testing device: {str(e)}")
        return False

def main():
    """
    Main function to test quantum devices.
    """
    # List all devices
    devices = list_all_devices()
    
    if not devices:
        return
    
    # Ask user if they want to test devices
    response = input("\nDo you want to test any devices? (y/n): ")
    if response.lower() != 'y':
        return
    
    # Ask user which device to test
    print("\nAvailable devices:")
    for i, device in enumerate(devices, 1):
        print(f"{i}. {device.name} ({device.provider_name}) - {device.status}")
    
    try:
        device_index = int(input("\nEnter the number of the device to test (0 to test all): ")) - 1
        
        if device_index == -1:
            # Test all devices
            for device in devices:
                test_device(device)
                time.sleep(2)  # Wait between tests
        elif 0 <= device_index < len(devices):
            # Test selected device
            test_device(devices[device_index])
        else:
            print("Invalid device number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main() 