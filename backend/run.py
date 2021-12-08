from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.responses import RedirectResponse
from config.db import db
from routes import *

# Routes
from routes.geocaches import geocaches
from routes.logbooks import logbooks

app = FastAPI()
app.include_router(geocaches)
app.include_router(logbooks)

@app.get("/")
def read_root():
    return RedirectResponse(url='/docs')

# Allow all Origins
app = CORSMiddleware(
    app=app,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)