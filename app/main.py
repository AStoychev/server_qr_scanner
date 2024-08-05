from fastapi import FastAPI
from routers import user, admin_user

app = FastAPI()

app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(admin_user.router, prefix="/admin_user", tags=["AdminUser"])

@app.get("/")
async def root():
    print("Server is starting!")
    return {"message": "Welcome to the FastAPI MongoDB Application!"}

