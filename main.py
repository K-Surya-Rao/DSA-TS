from fastapi import FastAPI
from routers import twosum

app = FastAPI()

app.include_router(twosum.router)


@app.get("/")
def root():
    return {"message": "DSA API - Available endpoints: /twosum"}