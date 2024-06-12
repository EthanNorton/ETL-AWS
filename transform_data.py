import boto3
import json
import os
import spark 
from pyspark.sql import SparkSession # learning about pyspark for efficient data loading
# would be interested in finding out how to lower processing time in spark for quicker reports, for example 

def transform_data():
    # Define S3 buckets and prefixes
    s3_bucket = 'your-s3-bucket'
    raw_prefix = 'raw/package_data/'
    processed_prefix = 'processed/package_data/'
    
    # Initialize S3 client
    s3_client = boto3.client('s3')
    
    # List objects in the raw data prefix
    response = s3_client.list_objects_v2(Bucket=s3_bucket, Prefix=raw_prefix)
    if 'Contents' not in response:
        print("No raw data files found")
        return
    ## Usually deal with nulls, check for missing data
    ## Visualiation, EDA
    ## Look for wrong naming conventions 
    ## maybe feature engineering, if that is a request
    ## clean abstract names from S3 into readable variables and apply OOP and modularity 

    
    for obj in response['Contents']:
        key = obj['Key']
        
        # Get the raw data
        raw_data = s3_client.get_object(Bucket=s3_bucket, Key=key)
        raw_data_str = raw_data['Body'].read().decode('utf-8')
        raw_data_json = json.loads(raw_data_str)
        
        # Example transformation: Categorize delivery exceptions
        transformed_data = []
        for record in raw_data_json:
            if record['status'] in ['delivered', 'in_transit']:
                record['exception'] = False
            else:
                record['exception'] = True
            transformed_data.append(record)
        
        # Convert transformed data to JSON
        transformed_data_json = json.dumps(transformed_data)
        
        # Save transformed data to S3
        processed_key = key.replace(raw_prefix, processed_prefix)
        s3_client.put_object(Bucket=s3_bucket, Key=processed_key, Body=transformed_data_json)
        
        print(f"Data transformed and saved to {processed_key}")

if __name__ == '__main__':
    transform_data()
