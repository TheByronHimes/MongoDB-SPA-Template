import os
from fastapi import FastAPI
from pymongo import MongoClient

# Import Username & Password from container env vars
DB_USERNAME = os.environ["db_username"]
DB_PASSWORD = os.environ["db_password"]

# Create connection to DB
client = MongoClient(
    host="mongodb://mongo:27017", username=DB_USERNAME, password=DB_PASSWORD
)

# Set up the FastAPI entrypoint
app = FastAPI()

@app.get("/")
async def root():
    msg = "Hello World!"
    return {"msg": msg}
