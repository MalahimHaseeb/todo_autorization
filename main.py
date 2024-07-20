from fastapi import FastAPI 
from routes.userRoute import userr
from routes.todoRoute import todor
from dotenv import load_dotenv
load_dotenv()
app = FastAPI(title="CRUD")

app.include_router(userr)
app.include_router(todor) 
