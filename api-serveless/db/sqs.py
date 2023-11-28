import boto3
import json
from .db_connection import get_app_db
cola_de_mensaje=boto3.client('sqs')
incoming_queue_url = 'URL_de_tu_cola_entrante_SQS'
processed_queue_url = 'URL_de_tu_cola_procesada_SQS'
def lambda_handler(event, context):
    app_db=get_app_db()
    try:
       response=cola_de_mensaje.receive_message(
           QueueUrl=incoming_queue_url,
           MaxNumberOfMessages= 5
       )
       if 'Message' in response:
           for message in response['Message']:
               message_body=json.loads(message['Body'])
     
               #Guardar en dynamodb
               app_db.put_item(
                   Item={
                       'id':message_body['id'],
                       'title': message_body['title']
     
     
                   }
               )
     
               # enviar el mensaje proceasdo a la cola de mensaje procesados
               cola_de_mensaje.send_message(
                   QueueUrl=processed_queue_url,
                   MessageBody=message['Body']
               )
     
               #elimar el mensaje de la cola sqs de entrada
               cola_de_mensaje.dele_message(
                   QueueUrl=incoming_queue_url,
                   ReceiptHandler=message['ReceiptHandler']
               )

    except Exception as e:
        print(f'error:{e}')




