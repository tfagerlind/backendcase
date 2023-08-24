"""A webhook listener service."""

from http import HTTPStatus
import json
import logging
from flask import Flask, request, abort, jsonify
from jsonschema import validate, ValidationError
from pymongo import MongoClient

SCHEMA_PATH = 'schema.json'

CONNECTION_STRING = "mongodb://root:example@mongo"


def get_collection():
    """Get the collection of events."""
    client = MongoClient(CONNECTION_STRING)
    database = client['webhook']
    collection = database['events']

    return collection


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


@app.get('/')
def get():
    """List the events of the database."""
    collection = get_collection()

    items = collection.find()
    items_as_json = []
    for item in items:
        copy = item.copy()
        copy.pop('_id')
        items_as_json.append(copy)

    app.logger.info(json.dumps(items_as_json, indent=1))

    return "<pre>" + json.dumps(items_as_json, indent=1) + "</pre>"


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

    collection = get_collection()

    collection.insert_one(data)

    return jsonify({'success': True})
