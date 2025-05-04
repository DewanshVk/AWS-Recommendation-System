import boto3
import json

# Initialize DynamoDB resource and table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('storeRecommendations')

def lambda_handler(event, context):
    # Log function start and event for debugging
    print("Lambda function started")
    print("Received event:", json.dumps(event))

    # Ensure the event contains 'userId' and 'recommendations'
    user_id = event.get("userId")
    recommendations = event.get("recommendations", [])

    # Check if userId is missing
    if not user_id:
        print("Error: Missing 'userId' in event")
        return {
            'statusCode': 400,
            'body': "Missing 'userId' in event"
        }

    # Check if recommendations list is empty
    if not recommendations:
        print("Error: Missing or empty 'recommendations' in event")
        return {
            'statusCode': 400,
            'body': "Missing or empty 'recommendations' in event"
        }

    # Prepare the item to be stored in DynamoDB
    item = {
        'user_id': user_id,
        'recommendations': recommendations
    }

    # Insert data into DynamoDB
    try:
        print(f"Storing data in DynamoDB: {item}")
        response = table.put_item(Item=item)
        print("DynamoDB response:", response)

        # Return success response
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Data stored successfully!',
                'dynamoResponse': response
            })
        }
    except Exception as e:
        print(f"Error storing data in DynamoDB: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': f"Failed to store data: {str(e)}"
            })
        }
