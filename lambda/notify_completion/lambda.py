def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": "Workflow completed.",
        "userId": event.get("userId")
    }
