from fastapi import FastAPI

from cats_api.api import router

app = FastAPI()

app.include_router(router)
