from fastapi import FastAPI, HTTPException
from models import Item
from controllers import create_item, get_all_items, update_item, delete_item, one_item
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:80",
    "http://localhost:8000",    
]

#autorização para que outros ips acessem meu site
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.post("/items/")
def add_item(item: Item):
    return create_item(item)

@app.get("/items/{item_id}")
def read_one_item(item_id: int):
   return one_item(item_id)

@app.get("/items/")
def read_items():
    return get_all_items()

@app.put("/items/{item_id}")
def update_item_details(item_id: str, item: Item):
    return update_item(item_id, item)

@app.delete("/items/{item_id}")
def remove_item(item_id: str):
    return delete_item(item_id)
