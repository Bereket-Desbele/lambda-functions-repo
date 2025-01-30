import json
import numpy as np  # External dependency

def lambda_handler(event, context):
    array = np.array([1, 2, 3])
    return {
        "statusCode": 200,  # Required
        "headers": {        # Required for CORS
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type,Authorization",
            "Content-Type": "application/json"
        },
        "body": json.dumps({  # Must be string
            "message": array.tolist()
        })
    }