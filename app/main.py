from fastapi import FastAPI, Request
from app.routes.home import router as home_router
from app.routes.chat_route import router as chat_router
from app.config.settings import APP_NAME, DEBUG

app = FastAPI()

app.include_router(home_router) #FastAPI registers the router.
app.include_router(chat_router) 