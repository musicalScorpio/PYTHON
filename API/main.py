from fastapi import FastAPI

app = FastAPI()
#uvicorn main:app --reload https://www.uvicorn.org
@app.get("/retriveAnswer/{question}")
async def root():

    return {"message": "Hello World 123"}