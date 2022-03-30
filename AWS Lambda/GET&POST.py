import json

def lambda_handler(event, context):
    first,sec,operator=0,0,"add"
    http_method=event['httpMethod']
    
    if http_method=='GET':
        first=int(event['queryStringParameters']['first'])
        sec=int(event['queryStringParameters']['sec'])
        operator=event['queryStringParameters']['operator']
    elif http_method=='POST':
        body=json.loads(event['body'])
        first=int(body['first'])
        sec=int(body['sec'])
        operator=body['operator']
    return {
        'statusCode': 200,
        'body': json.dumps(calculate(first,sec,operator))
    }

def calculate(first,sec,operator):
    if (operator=="add"):
        res=first+sec
    elif (operator=="sub"):
        res=first-sec
    elif (operator=="multiply"):
        res=first*sec
    elif(operator=="divide"):
        if sec!=0:
            res=first//sec
    return res