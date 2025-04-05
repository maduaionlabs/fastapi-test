from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
async def root():
    print(os.environ)
    api_key = os.getenv("AZURE_OPENAI_ENDPOINT")
    return {"message": f"api key - {api_key}"}