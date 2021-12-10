from fastapi import APIRouter, status, Response
from config.db import db
from services import logbook_service
from models.logbook import Logbook
from services.logbook_service import delete_logbook, update_logbook

from bson import json_util

from utils.utils import to_json

import json

logbooks = APIRouter()

@logbooks.get("/logbooks")
async def read_logbooks():
    logbooks = logbook_service.get_all_logbooks()
    
    try:    
        return logbooks
    except:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@logbooks.get("/logbooks/{logbook_id}")
async def read_logbook(logbook_id):
    logbook = logbook_service.get_logbook(logbook_id)

    if not logbook:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    return logbook


@logbooks.post("/logbooks")
async def create_logbook(logbook: Logbook):
    logbook = logbook_service.create_logbook(logbook)
    
    if not logbook:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    
    return logbook
                

@logbooks.put("/logbooks/{logbook_id}")
async def update_logbook(logbook_id, logbook: Logbook):
    logbook = logbook_service.update_logbook(logbook_id, logbook)
    
    if not logbook:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    return logbook
                

@logbooks.delete("/logbooks/{logbook_id}")
async def delete_logbook(logbook_id):
    logbook = delete_logbook(logbook_id)
    
    if logbook:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    
    return logbook
