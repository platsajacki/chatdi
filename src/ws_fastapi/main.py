import ws_fastapi._django_setup  # noqa: F401
from fastapi import FastAPI

from ws_fastapi.conversations.router import router as conversations_router

app = FastAPI()
app.include_router(conversations_router, tags=['conversations'])
