# PathFinder - Backend API
# DSN x BCT Hackathon 3.0
# Team: oladelegoodness470-dot

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="PathFinder API")

@app.get("/")
def home():
    return {"message": "PathFinder API is running!"}
