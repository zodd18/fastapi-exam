import json
from db import db

collection = db['Collection']

# Delete all documents from collection
collection.delete_many({})


# Insert all documents from json file into collection
with open('./collection.json') as f:
    data = json.load(f)
    for item in data:
        collection.insert_one(item)