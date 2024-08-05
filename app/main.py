from fastapi import FastAPI
from routers import user
from database import users_collection, admin_users_collections

app = FastAPI()

app.include_router(user.router, prefix="/user", tags=["user"])


@app.get("/")
async def root():
    print('Server is starting!')
    return {"message": "Welcome to the FastAPI MongoDB Application!"}
