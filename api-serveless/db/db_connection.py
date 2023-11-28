import boto3

def get_app_db():
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table('my--table')
    return table