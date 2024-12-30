from fastapi import FastAPI
import uvicorn

from src.engine import entity_recognition

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/ner/{text}")
async def ner(text: str):
    return entity_recognition(text)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
