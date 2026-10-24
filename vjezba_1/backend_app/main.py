from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str

items = [{"id": 1, "name": "Prva stavka"}]

@app.get("/")
def root():
    return {"poruka": "API radi"}

@app.get("/items")
def get_items():
    return items

@app.post("/items", status_code=201)
def add_item(item: Item):
    new = {"id": len(items) + 1, "name": item.name}
    items.append(new)
    return new

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i in items:
        if i["id"] == item_id:
            items.remove(i)
            return {"obrisano": item_id}
    raise HTTPException(status_code=404, detail="Nema te stavke")