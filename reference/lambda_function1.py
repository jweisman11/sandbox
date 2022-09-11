import json

def lambda_handler(event, context):
    # TODO implement
    try:
        comment = event['Comment']
    except:
        comment = ''
    
    comment = comment + '... action from Lambda 1'
    
    return {
        'statusCode': 200,
        'body': comment
    }