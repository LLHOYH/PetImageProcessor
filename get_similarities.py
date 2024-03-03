import boto3
import csv
import io
import json
import requests
import numpy as np
from numpy.linalg import norm

s3 = boto3.client('s3')


def calculateSimilarities():
    
    # define two lists or array
    A = np.array([2,1,2,3,2,9])
    B = np.array([3,4,2,4,5,5])
    
    print("A:", A)
    print("B:", B)
    
    # compute cosine similarity
    cosine = np.dot(A,B)/(norm(A)*norm(B))
    print("Cosine Similarity:", cosine)

def sendSMS(phone_number):
    
    url = 'https://1d7eqpxzki.execute-api.ap-southeast-2.amazonaws.com/Dev/SMS-sender'
    headers = {'Content-Type': 'application/json'}  # Specify the content type as JSON
    payload = {
        'phone_number':'+61468431079'
        'message':'morning'
        'sender':'WheresMyPet'
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        # Process the API response data
        api_data = response.json()
        print('API response:', api_data)
        return {
            'statusCode': 200,
            'body': api_data
        }