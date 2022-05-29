from typing import Union
from fastapi import FastAPI
from config import Settings

settings = Settings()
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }