from .db_connection import get_app_db

def add_book_to_db(data):
    try:
        get_app_db().put_item(Item={
            'id': data['id'],
            'title': data['title'],
            'author': data['author'],
            'published_year': data['published_year']
        })
        return {'message': 'ok - CREATED', 'status': 201, 'id': data['id'], 'title': data['title'], 'author': data['author'], 'published_year': data['published_year']}
    except Exception as e:
        return {'message': str(e)}

def get_all_books():
    response = get_app_db().scan()
    data = response.get('Items', None)
    return {'data': data}

def get_book_by_id(id):
    response = get_app_db().query(
        KeyConditionExpression=Key('id').eq(id)
    )
    data = response.get('Items', None)
    return {'data': data}

def update_book(data):
    try:
        get_app_db().update_item(
            Key={
                'id': data['id'],
                'author': data['author']
            },
            UpdateExpression='set title=:r',
            ExpressionAttributeValues={
                ':r': data['title']
            },
            ReturnValues='UPDATED_NEW'
        )
        return {'message': 'ok - UPDATED', 'status': 201}
    except Exception as e:
        return {'message': str(e)}

def delete_book(id):
    try:
        response = get_app_db().delete_item(
            Key={'id': id}
        )
        return {'message': 'ok - DELETED', 'status': 201}
    except Exception as e:
        return {'message': str(e)}