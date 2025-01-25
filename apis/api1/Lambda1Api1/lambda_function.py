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
        "statusCode": 200,  # Required
        "headers": {        # Required for CORS
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type,Authorization",
            "Content-Type": "application/json"
        },
        "body": json.dumps({  # Must be string
            "message": parsed_content
        })
    }

