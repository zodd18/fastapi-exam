from fastapi import APIRouter, responses
from bson import ObjectId, json_util
import pymongo
import json

from config.db import db

users = APIRouter()

@users.get("/users")
async def read_users():
    users = db.User.find()
    response = json_util.dumps(users)
    return json.loads(response)

@users.get("/users/{user_id}")
async def read_user(user_id: str):
    try:
        user = db.User.find_one({"_id": ObjectId(user_id)})
    except:
        user = db.User.find_one({"username": user_id})
        if not user: 
            user = db.User.find_one({"email": user_id})
    
    response = json_util.dumps(user)

    return json.loads(response)

@users.post("/users")
async def create_user(user: dict):
    if db.User.find_one({"username": user["username"]}) or db.User.find_one({"email": user["email"]}):
        return {"message": "Username or email already in use"}

    user_id = db.User.insert_one(user).inserted_id
    return {"user_id": str(user_id)}

@users.put("/users/{user_id}")
async def update_user(user_id: str, user: dict):
    repeated_username = db.User.find_one({"username": user["username"]})
    if repeated_username and repeated_username["_id"] != ObjectId(user_id):
        return {"message": "Username already in use"}

    repeated_email = db.User.find_one({"email": user["email"]})
    if repeated_email and repeated_email["_id"] != ObjectId(user_id):
        return {"message": "Email already in use"}

    db.User.update_one({"_id": ObjectId(user_id)}, {"$set": user})
    return {"user_id": user_id}

@users.delete("/users/{user_id}")
async def delete_user(user_id: str):
    db.User.delete_one({"_id": ObjectId(user_id)})
    return {"user_id": user_id}

@users.delete("/users")
async def delete_users():
    db.User.delete_many({})
    return {"message": "Users deleted"}
