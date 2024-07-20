from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os

# Corrected usage of os.getenv
mongo_url = os.getenv("MONGO_URL")
if mongo_url is None:
    raise ValueError("Environment variable MONFO_URL not set")

MongoClient = MongoClient(mongo_url)
db = MongoClient.UserData 
cl = db.users
todocl = db.todos 