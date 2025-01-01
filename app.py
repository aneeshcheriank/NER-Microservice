from fastapi import FastAPI
import uvicorn

from src.ner import ner as entity_recognition

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ner/{query}")
async def ner(query: str):
    return entity_recognition(query)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
