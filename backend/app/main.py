from fastapi import FastAPI  # type: ignore[import]
from app.database import engine, Base
from app.routes.auth import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Backend Running"}