from bson.objectid import ObjectId
from config.db import db
from models.geocache import Geocache
from utils.utils import to_json

from passlib.hash import sha256_crypt

from services import logbook_service

def get_all_geocaches():
    return to_json(db.Geocache.find())

def get_geocache(id):
    try:
        return to_json(db.Geocache.find_one({'_id': ObjectId(id)}))
    except:
        return None

def get_logbooks_by_email(email):
    logbooks = db.logbook.find({'email': email})
    
    return to_json([get_geocache(logbook['geocache_id']) for logbook in logbooks])

def get_geocaches_by_hint(hint):
    return to_json(db.Geocache.find({'hint': hint}))

def get_not_found_geocaches():
    found_geocaches= set([logbook['geocache_id'] for logbook in logbook_service.get_all_logbooks()])
    
    return to_json([geocache for geocache in get_all_geocaches() if (geocache['_id']['$oid']) not in found_geocaches])
    

def create_geocache(geocache: Geocache):
    new_id = db.Geocache.insert_one(geocache.dict()).inserted_id
    
    return get_geocache(new_id)

def update_geocache(geocache_id, geocache: Geocache):
    if get_geocache(geocache_id) is None:
        return None
    
    db.Geocache.update_one({'_id': ObjectId(geocache_id)}, {'$set': geocache.dict()})
    
    return get_geocache(geocache_id)

def delete_geocache(id):
    db.Geocache.delete_one({'_id': ObjectId(id)})
    
    return get_geocache(id)