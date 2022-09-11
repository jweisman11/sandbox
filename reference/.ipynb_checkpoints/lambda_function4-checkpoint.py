import json
import boto3

sqs = boto3.client("sqs")

def lambda_handler(event, context):
    # TODO implement
    message = {"Name":"I am really cool"}
    queue_url = "https://queue.amazonaws.com/475434563362/weisman-sqs-test"
    
    resposne = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=.json.dumps(message),
        DelaySeconds=0)
    
    return {
        'statusCode': 200,
        'body': json.dumps("Hello from Lambda!")
    }