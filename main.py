from fastapi import FastAPI
from routers import twosum, threesum

app = FastAPI()

app.include_router(twosum.router)
app.include_router(threesum.router)

@app.get("/")
def root():
    return {"message": "DSA API - Available endpoints: /twosum"}