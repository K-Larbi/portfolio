from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # we’ll restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


client = MongoClient(os.getenv("MONGO_URI"))
db = client.portfolio_db

@app.get("/")
def root():
    return {"status": "Backend connected successfully 🚀"}

@app.get("/projects")
def get_projects():
    projects = list(db.projects.find({}, {"_id": 0}))
    return projects


