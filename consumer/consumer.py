import logging
from flask import Flask
from pymongo import MongoClient

CONNECTION_STRING = "mongodb://root:example@mongo"

def get_database():
   client = MongoClient(CONNECTION_STRING)

   app.logger.info("dbthings: %s", str(client))
   # Create the database for our example (we will use the same database throughout the tutorial
   #return client['user_shopping_list']


app = Flask(__name__)
app.logger.setLevel(logging.INFO)

get_database()

@app.get('/')
def get():
    dbname = get_database()
    #collection_name = dbname["user_1_items"]

    return "hello!"
