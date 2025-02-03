import json

def lambda_handler(event, context):
    a = 10
    b = 20
    c = a + b
    return {
        "statusCode": 200,
        "body": json.dumps({"result": c})
    }
