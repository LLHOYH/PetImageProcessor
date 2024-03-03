import os
import io
import boto3
import json
import csv
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
# import requests
# from IPython.core.display import HTML


# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
client= boto3.client('runtime.sagemaker')
region = boto3.Session().region_name
s3_bucket = f"jumpstart-cache-prod-{region}"
key_prefix = "inference-notebook-assets"
s3 = boto3.client("s3")

def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    
    return json.dumps("hi")
    data = json.loads(json.dumps(event))
    payload = data['data']
    
    # print(payload)
    
    queryResponse = query_endpoint(payload)
    queryResponse = client.invoke_endpoint(EndpointName=ENDPOINT_NAME, ContentType='application/x-image', Body=payload)
    
    model_predictions = json.loads(queryResponse['Body'].read())
    embedding = model_predictions['embedding']
    return embedding
