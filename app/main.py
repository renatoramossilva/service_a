from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"service": "A", "message": "Hello from Service A"}
