import boto3
from botocore.exceptions import ClientError
from datetime import datetime,timedelta
def generate_signed_url(buck_name,object_key):
    s3_cliente=boto.client('s3')
    expiration_time = 3600

    try:
        response=s3_cliente.generate_signed_url(
        'get_object',
        params={'Bucket':buck_name,'key':object_key},
        ExpiresIn=expiration_time
        )
        return {'status_code':200, 'signed_url':response}
    except ClientError as e:
        return {'status_Code':500,'error':str(e)}
