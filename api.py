from IPython.core.display import HTML

region = boto3.Session().region_name
s3_bucket = f"jumpstart-cache-prod-{region}"
key_prefix = "inference-notebook-assets"
s3 = boto3.client("s3")

def query_endpoint(img):
    endpoint_name = 'jumpstart-dft-efficientnet-lite1-fe-20240302-131428'
    client = boto3.client('runtime.sagemaker')
    response = client.invoke_endpoint(EndpointName=endpoint_name, ContentType='application/x-image', Body=img)
    return response

def parse_response(query_response):
    model_predictions = json.loads(query_response['Body'].read())
    embedding = model_predictions['embedding']
    return embedding