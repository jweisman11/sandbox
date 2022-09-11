import json

def lambda_handler(event, context):
    # TODO implement
    try:
        comment = event['Comment']
    except:
        comment = ''
    
    comment = comment + '... action from Lambda 2'
    
    return {
        'statusCode': 200,
        'body': comment
    }