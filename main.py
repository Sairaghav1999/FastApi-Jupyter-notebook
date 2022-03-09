from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    Location: str
    Date: str
    Time: str
app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return 'hello world'
