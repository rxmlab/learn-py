
import os
import uvicorn
from fastapi import FastAPI
from app.database import engine
from app.database import Base

from app.models import user
from app.routes import user_routes

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(user_routes.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Inventory Management API"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

