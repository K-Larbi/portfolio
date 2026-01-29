from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

client = MongoClient(os.getenv("MONGO_URI"))
db = client.portfolio_db

@app.get("/")
def root():
    return {"status": "Backend connected successfully 🚀"}

@app.get("/projects")
def get_projects():
    projects = list(db.projects.find({}, {"_id": 0}))
    return projects
