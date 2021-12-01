import os
import bson
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from bson import ObjectId, json_util
import pymongo

# routes
from routes.users import users

app = FastAPI()
app.include_router(users)

@app.get("/")
def read_root():
    return {"Hello": "World"}
