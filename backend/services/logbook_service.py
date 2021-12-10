from bson.objectid import ObjectId
from config.db import db
from models.logbook import Logbook

from passlib.hash import sha256_crypt

from utils.utils import to_json

from services import geocache_service

def get_all_logbooks():
    return to_json(db.logbook.find())

def get_logbook(id):
    try:
        return to_json(db.logbook.find_one({'_id': ObjectId(id)}))
    except:
        return None

def create_logbook(logbook: Logbook):
    new_id = db.logbook.insert_one(logbook.dict()).inserted_id
    return get_logbook(new_id)

def update_logbook(logbook_id, logbook: Logbook):
    db.logbook.update_one({'_id': ObjectId(logbook_id)}, {'$set': logbook.dict()})
    return get_logbook(logbook_id)

def delete_logbook(id):
    db.logbook.delete_one({'_id': ObjectId(id)})
    return get_logbook(id)

def get_logbooks_by_geocache(geocache_id):
    return to_json(db.logbook.find({'geocache_id': ObjectId(geocache_id)}))