import json
import boto3

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('EcommerceUsers')

def lambda_handler(event, context):
    bucket = 'ecommerce-user-data-bucket'
    key = 'ecommerce_users.json'

    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')
    users = json.loads(content)

    for user in users:
        table.put_item(Item=user)

    # Get userId of the first user to pass forward
    user_id = users[0].get("userId") if users and "userId" in users[0] else None

    return {
        'statusCode': 200,
        'body': f"Successfully inserted {len(users)} users into DynamoDB",
        'userId': user_id  # <-- Add this line
    }
