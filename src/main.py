from fastapi import FastAPI

fast_api_app :FastAPI = FastAPI()

@fast_api_app.get("/")
async def root():
    return {"message" : "Hello Karthik, Welcome to Multiverse!"}

@fast_api_app.get("/names")
async def minaami():
    return {"message" : "Gulte"}    