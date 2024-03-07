from fastapi import FastAPI

app = FastAPI(
    title="Python FastAPI Workshop",
    description="Welcome to workshop on Python Programming.",
)


@app.get("/info", tags=["App Info"])
def get_info():
    return {"app": "Python Workshop", "version": "0.0.1", "author": "Tushar Velingkar"}
