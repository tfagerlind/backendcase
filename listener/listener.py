from http import HTTPStatus
import json
import logging
import time
from flask import Flask, request, abort
from jsonschema import validate, ValidationError

SCHEMA_PATH = 'schema.json'

def data_is_valid(data):
    with open(SCHEMA_PATH) as schema_file:
        schema = json.load(schema_file)

    try:
        validate(instance=data, schema=schema)
        return True
    except ValidationError:
        return False

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

@app.get('/')
def get():
    return "hello!"

@app.post('/')
def webhook_post():
    if not request.is_json:
        app.logger.info('Invalid request.')
        abort(HTTPStatus.BAD_REQUEST)

    data = request.get_json()

    if not data_is_valid(data):
        app.logger.info('Invalid request.')
        abort(HTTPStatus.BAD_REQUEST)

    app.logger.info('Valid request: %s', str(data))
    return {}
