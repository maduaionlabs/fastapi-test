from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
async def root():
    print(os.environ)
    api_key = os.getenv("INTERNAL_API_KEY")
    return {"message": f"api key - {api_key}"}