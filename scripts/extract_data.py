## This file I do not have access to tools, but helps me understand to compare to previous experiences 

import boto3
import json
import os 
from datetime import datetime
from dotenv import load_dotenv # if dotenv is in AWS stack, and there are API calls or sensitive info there 

# Load variables from the .env file into environment variables
load_dotenv()

def extract_data():
    # Define S3 bucket and prefix 
    s3_bucket = 'your-s3-bucket'
    s3_prefix = 'raw/package_data/'
    
    # Initialize S3 client
    s3_client = boto3.client('s3')
    
    # Example: Simulated data extraction
    data = [
        {'package_id': '123', 'status': 'delivered', 'timestamp': str(datetime.now())},
        {'package_id': '456', 'status': 'in_transit', 'timestamp': str(datetime.now())},
        # Add more records as needed
    ]
    
    # Convert data to JSON
    # I do have experience with JSON reading and connecting via request, boto3 and s3 are similar in AWS.
    data_json = json.dumps(data)
    
    # Save data to S3
    file_name = f"package_data_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
    s3_client.put_object(Bucket=s3_bucket, Key=f"{s3_prefix}{file_name}", Body=data_json)
    
    print(f"Data extracted and saved to {s3_prefix}{file_name}")

    # Apply rules to each step to ensure data is clean, handle edge cases in terms of file not reading
    # and other error messages possible
    
if __name__ == '__main__':
    extract_data()
  # rename to csv files for next step
