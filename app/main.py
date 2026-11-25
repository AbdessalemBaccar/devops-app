from fastapi import FastAPI, HTTPException

app = FastAPI(title="devops-app")

ITEMS = {1: "book", 2: "pen"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/item/{item_id}")
def get_item(item_id: int):
    if item_id not in ITEMS:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, "name": ITEMS[item_id]}


@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}
