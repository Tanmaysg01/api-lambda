import json
import os
import boto3
import csv

s3_client = boto3.client('s3')

def lambda_handler(event,  context):
    bucket_name = "input-api-bucket"
    file_name = "Book1.csv"
    s3_response = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    print("s3_response:", s3_response)    
    file_data = s3_response["Body"].read().decode('utf')
    print("file_data:",file_data)
    return str(file_data).upper()