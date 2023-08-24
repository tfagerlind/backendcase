"""A webhook listener service."""

from http import HTTPStatus
import json
import logging
from flask import Flask, request, abort
from jsonschema import validate, ValidationError
from pymongo import MongoClient

SCHEMA_PATH = 'schema.json'

CONNECTION_STRING = "mongodb://root:example@mongo"


def get_database():
    """Get the database."""
    client = MongoClient(CONNECTION_STRING)
    database = client['webhook']
    collection = database['events']
    app.logger.info("dbthings: %s", str(client))
    app.logger.info("databases: %s", client.list_database_names())
    items = collection.find()
    for item in items:
        app.logger.info("item: %s", item)

    collection.insert_one({'foo': 'bar'})

    return database


def event_is_valid(data):
    """Check if the structure of the event is valid"""
    with open(SCHEMA_PATH, encoding="utf-8") as schema_file:
        schema = json.load(schema_file)

    try:
        validate(instance=data, schema=schema)
        return True
    except ValidationError:
        return False


app = Flask(__name__)
app.logger.setLevel(logging.INFO)

get_database()


@app.get('/')
def get():
    """List the events of the database."""
    get_database()
    # collection_name = dbname["user_1_items"]

    return "hello!"


@app.post('/')
def webhook_post():
    """Register webhook events."""
    if not request.is_json:
        app.logger.info('Invalid request.')
        abort(HTTPStatus.BAD_REQUEST)

    data = request.get_json()

    if not event_is_valid(data):
        app.logger.info('Invalid request.')
        abort(HTTPStatus.BAD_REQUEST)

    app.logger.info('Valid request: %s', str(data))
    return {}
