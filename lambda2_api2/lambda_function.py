import json
import pandas as pd  # External dependency

def lambda_handler(event, context):
    data = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data)
    return {
        'statusCode': 200,
        'body': df.to_json(orient='split')
    }
