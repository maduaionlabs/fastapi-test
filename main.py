from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
async def root():
    os.getenv("")
    return {"message": "Hello World"}