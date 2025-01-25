import json
from bs4 import BeautifulSoup  # External dependency

def lambda_handler(event, context):
    html_doc = "<html><head><title>Test</title></head><body></body></html>"
    soup = BeautifulSoup(html_doc, 'html.parser')
    return {
            "statusCode": 200,  # Required
            "headers": {        # Required for CORS
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type,Authorization",
                "Content-Type": "application/json"
            },
            "body": json.dumps({  # Must be string
                "message": {'title': soup.title.string}
            })
    }
