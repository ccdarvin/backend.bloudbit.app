from dataclasses import dataclass
from typing import Union

from fastapi import FastAPI


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