import json


def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def helloo(event, context):
    body = {
        "message": "hello world",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
