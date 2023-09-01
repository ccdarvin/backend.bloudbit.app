from dataclasses import dataclass
from typing import Union

from fastapi import FastAPI
from apps.db import init_db
from apps.auth.models import *

app = FastAPI()


@dataclass
class Root:
    message: str
    version: str
    url: str


@app.get("/")
def get_root() -> Root:
    return Root(
        message="Backend API",
        version="1.0.0",
        url="backend.example.com",
    )
    
@app.on_event("startup")
async def startup_event():
    await init_db()
