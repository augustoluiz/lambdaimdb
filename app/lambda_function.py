import json
from pathlib import Path

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": {
            'id': 123
        }
    }
