"""A webhook listener service."""

from datetime import datetime
from http import HTTPStatus
import json
import logging
from flask import Flask, request, abort, jsonify
from jsonschema import validate, ValidationError
import pymongo
from pymongo import MongoClient

SCHEMA_PATH = 'schema.json'

CONNECTION_STRING = "mongodb://root:example@mongo"

EXPIRE_AFTER_SECONDS = 60 * 60 * 24 * 7  # one week

MAX_DOCUMENTS = 1000


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
    """List the events of the database.

    The events are listed in the opposite order that they came, i.e the last
    event is listed first. The number of documents listed has a limit.
    """

    def remove_internal_fields(document):
        document.pop('_id')
        document.pop('createdAt')

        return document

    collection = get_collection()
    documents = collection.find().sort(
        [("createdAt", pymongo.DESCENDING)]).limit(MAX_DOCUMENTS)

    documents_as_json = [remove_internal_fields(document.copy())
                         for document
                         in documents]

    return "<pre>" + json.dumps(documents_as_json, indent=1) + "</pre>"


@app.post('/event')
def event_post():
    """Register webhook events."""
    if not request.is_json:
        app.logger.info('Invalid request.')
        abort(HTTPStatus.BAD_REQUEST)

    event = request.get_json()

    if not event_is_valid(event):
        app.logger.info('Invalid request.')
        abort(HTTPStatus.BAD_REQUEST)

    app.logger.info('Valid request: %s', str(event))

    # Add a time stamp to each event for traceability and in order to keep
    # track of lifetime.
    event_with_timestamp = event.copy()
    event_with_timestamp["createdAt"] = datetime.now()

    # Store event. Ensure that documents are automatically removed eventually.
    # See https://devpress.csdn.net/mongodb/630464f6c67703293080c4f9.html
    #
    # It is ugly to recreate index for every insert but it works.
    collection = get_collection()
    collection.create_index([("createdAt", pymongo.ASCENDING)],
                            expireAfterSeconds=EXPIRE_AFTER_SECONDS)
    collection.insert_one(event_with_timestamp)

    return jsonify({'success': True})


@app.post('/clear')
def clear_post():
    """Clear all webhook events."""

    get_collection().drop()

    return jsonify({'success': True})
