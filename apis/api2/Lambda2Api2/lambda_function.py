import json
import pandas as pd  # External dependency

def lambda_handler(event, context):
    data = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data)
    return {
        "statusCode": 200,  # Required
        "headers": {        # Required for CORS
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type,Authorization",
            "Content-Type": "application/json"
        },
        "body": json.dumps({  # Must be string
            "message": df.to_json(orient='split')
        })
    }