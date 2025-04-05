from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
async def root():
    print(os.environ)
    api_key = os.getenv("test_variable")
    return {"message": f"api key - {api_key}"}