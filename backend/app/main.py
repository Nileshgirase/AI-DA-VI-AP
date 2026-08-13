from fastapi import FastAPI  # type: ignore[import]

from fastapi.middleware.cors import CORSMiddleware # type: ignore[import]

from app.routes.upload import router as dataset_router # type: ignore[import]

from app.models.user import User

from app.models.dataset import Dataset

from app.database import engine, Base

from app.routes.auth import router

from app.routes.auth import router as auth_router

from app.routes.upload import router as dataset_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)
app.include_router(dataset_router)

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