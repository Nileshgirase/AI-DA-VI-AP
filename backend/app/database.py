from sqlalchemy import create_engine  # type: ignore[reportMissingImports]
from sqlalchemy.ext.declarative import declarative_base  # type: ignore[reportMissingImports]
from sqlalchemy.orm import sessionmaker  # type: ignore[reportMissingImports]

DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()