from fastapi import APIRouter, FastAPI, Request

router  = APIRouter() #FastAPI provides two main objects:app = FastAPI()router = APIRouter()
#This router will own all routes in this file.
@router.get("/")
def home():
    return {"message": "Welcome to the AI Career Assistant!"}

