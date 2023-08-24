import json
import time
from flask import Flask, request
from jsonschema import validate

SCHEMA_PATH = 'schema.json'

def validate_data(data):
    with open(SCHEMA_PATH) as schema_file:
        schema = json.load(schema_file)

    validate(instance=data, schema=schema)

app = Flask(__name__)

@app.get('/')
def get():
    return "hello!"

@app.post('/')
def webhook_post():
    print("YESSWS!!!")
    data = request.get_json()
    print("json: " + str(data))
    validate_data(data)
    return {}
