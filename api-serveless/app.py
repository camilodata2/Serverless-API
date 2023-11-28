# app.py
from chalice import Chalice
from db.book_functions import add_book_to_db, delete_book
from db.book_functions import get_all_books, get_book_by_id, update_book
from db.url import generate_signed_url
from db.thumbnail import lambda_handler,resize_image
from db.sqs import lambda_handler
app = Chalice(app_name='api-serveless')

@app.on_s3_event(bucket='chalice-s3-thumbnail-demo',prefix='/images',suffix='.jpng')
def s3_event(event,context):
    return lambda_handler(event,context)
@app.route('/generate_signed_url/{bucket}/{key}')
def  generate_url(bucket, Key):
    return generate_signed_url(bucket,Key)

@requires_auth
@app.route('/book', methods=['POST'])

def add_book():
    data = app.current_request.json_body
    return add_book_to_db(data)

@app.route('/', methods=['GET'])
def index():
    return get_all_books()

@app.route('/book/{id}', methods=['GET'])
def get_book_id(id):
    return get_book_by_id(id)

@app.route('/book/{id}', methods=['PUT'])
def update_book_route(id):
    data = app.current_request.json_body
    data['id'] = id
    return update_book(data)

@app.route('/book/{id}', methods=['DELETE'])
def delete_book_route(id):
    return delete_book(id)

@app.on_sqs_message(queue='you-queue-name', batch_size=1)
def handler_sqs_message(event):
    return lambda_handler(event)

