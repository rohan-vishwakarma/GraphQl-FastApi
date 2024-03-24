from fastapi import FastAPI
from app.services import views

app = FastAPI()

# Mounting the example router
app.include_router(views.router)
