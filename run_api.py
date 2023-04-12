from fastapi import FastAPI
import asyncio
from colorama import init
from colorama import Fore, Back, Style
from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
from run_detection_function import det

app = FastAPI()

class Item(BaseModel):
    url: str
@app.post("/items/")
async def create_item(item: Item):
    url = item.url
    a = await asyncio.create_task(det(url))
    return a



# print(result)