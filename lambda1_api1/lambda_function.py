import json
import requests   # External dependency

def lambda_handler(event, context):
    response = requests.get("https://loripsum.net/api/")
    return {
        'statusCode': 200,
        'body': json.dumps(response.json())
    }
