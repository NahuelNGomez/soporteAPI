from fastapi import FastAPI
from routes.ticket import ticket

app = FastAPI()
app.include_router(ticket)
