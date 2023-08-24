import logging
from flask import Flask
from pymongo import MongoClient

CONNECTION_STRING = "mongodb://root:example@mongo"

def get_database():
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


app = Flask(__name__)
app.logger.setLevel(logging.INFO)

get_database()

@app.get('/')
def get():
    dbname = get_database()
    #collection_name = dbname["user_1_items"]

    return "hello!"
