from bson.objectid import ObjectId
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class Logbook(BaseModel):
    email: EmailStr
    geocache_id: str
    stamp: str