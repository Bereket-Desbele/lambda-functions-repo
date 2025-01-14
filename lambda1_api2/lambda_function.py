import json
from bs4 import BeautifulSoup  # External dependency

def lambda_handler(event, context):
    html_doc = "<html><head><title>Test</title></head><body></body></html>"
    soup = BeautifulSoup(html_doc, 'html.parser')
    return {
        'statusCode': 200,
        'body': json.dumps({'title': soup.title.string})
    }
