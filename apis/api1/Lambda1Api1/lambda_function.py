import json
import requests  # External dependency

def lambda_handler(event, context):
    response = requests.get("https://loripsum.net/api/")
    content = response.text  # Get the raw response content as a string
    
    try:
        # Try to parse the content as JSON
        parsed_content = response.json()
    except json.JSONDecodeError:
        # Handle the case where the response isn't JSON
        parsed_content = {"error": "Invalid JSON", "content": content}

    return {
        'statusCode': 200,
        'body': json.dumps(parsed_content)
    }
