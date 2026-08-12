from fastapi import FastAPI  # type: ignore[import]

from fastapi.middleware.cors import CORSMiddleware # type: ignore[import]

from app.database import engine, Base

from app.routes.auth import router

from app.models.dataset import Dataset

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Backend Running"}