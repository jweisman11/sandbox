import json
import boto3

s3 = boto3.client("s3")

def lambda_handler(event, context):
    # TODO implement
    message = event["Records"][0]["body"]
    
    s3.put_object(
        Bucket='weisman-sqs-test',
        Key="data.json",
        Body=json.dumps(message))
    
    return {
        'statusCode': 200,
        'body': json.dumps("Hello from Lambda!")
    }