from bson.objectid import ObjectId
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from typing import List, Optional

class Geocache(BaseModel):
    lat: float
    lon: float
    image: HttpUrl
    hint: str