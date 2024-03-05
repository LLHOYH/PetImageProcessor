import os
import io
import boto3
import json
import csv
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
import base64

# grab environment variables
ENDPOINT_NAME = "jumpstart-dft-efficientnet-lite1-fe-20240302-131428"
client= boto3.client('runtime.sagemaker')
region = boto3.Session().region_name
s3_bucket = f"jumpstart-cache-prod-{region}"
key_prefix = "inference-notebook-assets"
s3 = boto3.client("s3")


def lambda_handler(event, context):
    
    
    payload = str(event["body"])
    result = base64.b64decode(payload)
    print(result)
    print(type(result))

    queryResponse = client.invoke_endpoint(EndpointName=ENDPOINT_NAME, ContentType='application/x-image', Body=result)
    
    model_predictions = json.loads(queryResponse['Body'].read())
    embedding = model_predictions['embedding']
    return embedding