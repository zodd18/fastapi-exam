from fastapi import APIRouter, status, Response
from config.db import db
from services import geocache_service
from services import logbook_service
from models.geocache import Geocache
from services.geocache_service import delete_geocache, update_geocache
from typing import Optional

from bson import json_util

from utils.utils import response_json

import json

geocaches = APIRouter()

@geocaches.get("/geocaches")
async def read_geocaches(hint: Optional[str] = None, email: Optional[str] = None):
    geocaches = []
    
    if hint:
        geocaches = response_json(geocache_service.get_geocaches_by_hint(hint))
    elif email:
        geocaches = response_json(geocache_service.get_logbooks_by_email(email))
    else:    
        geocaches = response_json(geocache_service.get_all_geocaches())
    
    try:    
        return geocaches
    except:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@geocaches.get("/geocaches/{geocache_id}")
async def read_geocache(geocache_id):
    geocache = response_json(geocache_service.get_geocache(geocache_id))
    
    if not geocache:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    return geocache


@geocaches.post("/geocaches")
async def create_geocache(geocache: Geocache):
    geocache = geocache_service.create_geocache(geocache)
    
    if not geocache:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    
    return response_json(geocache)
                

@geocaches.put("/geocaches/{geocache_id}")
async def update_geocache(geocache_id, geocache: Geocache):
    geocache = geocache_service.update_geocache(geocache_id, geocache)
    
    if not geocache:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    return response_json(geocache)
                

@geocaches.delete("/geocaches/{geocache_id}")
async def delete_geocache(geocache_id):
    geocache = geocache_service.delete_geocache(geocache_id)
    
    if geocache:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    
    return response_json(geocache)


@geocaches.get("/geocaches/{geocache_id}/logbooks")
async def get_logbooks_by_geocache(geocache_id):
    logbooks = response_json(logbook_service.get_logbooks_by_geocache(geocache_id))
    
    if not logbooks:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    return logbooks

                
@geocaches.get("/geocaches/hint/{hint}")
async def get_geocaches_by_hint(hint):
    geocaches = response_json(geocache_service.get_geocaches_by_hint(hint))
    
    return geocaches
                

@geocaches.get("/geocaches/email/{email}")
async def get_geocaches_found_by_email(email):
    geocaches = response_json(geocache_service.get_logbooks_by_email(email))
    
    return geocaches

@geocaches.get("/geocaches-not-found")
async def get_geocaches_not_found():
    geocaches = response_json(geocache_service.get_not_found_geocaches())
    
    return geocaches
