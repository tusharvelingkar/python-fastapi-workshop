from fastapi import FastAPI
from routers import todos
import models
from database import engine

app = FastAPI(
    title="Python FastAPI Workshop",
    description="Welcome to workshop on Python Programming.",
)

models.Base.metadata.create_all(bind=engine)


@app.get("/info", tags=["App Info"])
def get_info():
    return {"app": "Python Workshop", "version": "0.0.1", "author": "Tushar Velingkar"}


app.include_router(todos.router)
