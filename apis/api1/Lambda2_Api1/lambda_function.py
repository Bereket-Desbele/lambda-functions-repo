import json
import numpy as np  # External dependency

def lambda_handler(event, context):
    array = np.array([1, 2, 3])
    return {
        'statusCode': 200,
        'body': json.dumps(array.tolist())
    }
