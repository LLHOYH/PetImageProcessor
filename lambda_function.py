import os
import io
import boto3
import json
import csv
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
import base64

# grab environment variables
ENDPOINT_NAME = os.environ["SageMakerEndPoint"]
client= boto3.client('runtime.sagemaker')
region = boto3.Session().region_name
s3_bucket = f"jumpstart-cache-prod-{region}"
key_prefix = "inference-notebook-assets"
s3 = boto3.client("s3")


def lambda_handler(event, context):
    
    
    payload = base64.b64decode(event["body"])

    queryResponse = client.invoke_endpoint(EndpointName=ENDPOINT_NAME, ContentType="application/x-image", Body=payload)
    model_predictions = json.loads(queryResponse['Body'].read())
    embedding = model_predictions['embedding']
    
    statusCode=500
    headers = {"Content-Type": "application/json"}
    body={}
    if embedding:
        statusCode = 200
        body=json.dumps({
            "embedding":embedding
        })
        
    response = {
        "statusCode":statusCode,
        "headers":headers,
        "body":body
    }
    return response
