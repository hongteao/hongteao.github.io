from typing import Dict, Any
from ast import Str
from email.policy import default
from typing import Dict, Optional
from fastapi import Depends, FastAPI
from pydantic import BaseModel
import uvicorn
from fastapi.encoders import jsonable_encoder
import json
from fastapi import Body, FastAPI

app = FastAPI()


class Item(BaseModel):
    id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None

@app.post("/items/", response_model=Item)
async def create_item(item: Item, key: str = Body(...)):
    print(item)
    fake_db[key] = item
    return item


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
