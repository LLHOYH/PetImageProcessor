import json
from datetime import datetime
from urllib.parse import parse_qs

def lambda_handler(event, context):
    
    # Parse query parameters from the event
    query_params = event['queryStringParameters']

    # Extract parameters from the query string
    postID = query_params['postID']
    poster = query_params['userID']
    image = query_params['image']
    category = query_params['category']
    place = query_params['place']

    # Process the parameters as needed
    time = datetime.now()

    # Construct response object
    response = {
        'postID': postID,
        'poster': poster,
        # Add more fields as needed
    }

    responseObject = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(response)
    }

    return responseObject
