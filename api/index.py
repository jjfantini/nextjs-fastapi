from fastapi import FastAPI

app = FastAPI()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

@app.get("/api/healthcheck")
def healthcheck():
    return {"status": "Check, Check, 1..2...!"}
