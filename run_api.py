from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
from function import det
import json

app = FastAPI()

class Item(BaseModel):
    url: str
    sequence: list

@app.post("/items/")
async def create_item(item: Item):
    url = item.url
    sequence = item.sequence
    # sequence = json.dumps(sequence)
    result = await asyncio.create_task(det(url, sequence))
    final_result_json = json.loads(result)
    return final_result_json

