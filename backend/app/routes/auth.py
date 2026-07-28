
from fastapi import APIRouter, Depends, HTTPException  # type: ignore[reportMissingImports]
from sqlalchemy.orm import Session #type: ignore[reportMissingImports]

from app.database import SessionLocal
from app.models.user import User

from app.schemas.user_schema import UserCreate, UserLogin
 

from app.services.auth_service import hash_password, verify_password


from app.utils.jwt_handler import create_access_token


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.email== user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail = "Email Already exists"
        )
    
    new_user = User(
        username =  user.username,
        email = user.email,
        password = hash_password(
            user.password
        )
    )

    db.add(new_user)
    db.commit()

    return{
        "message":"User registered successfully"
    }

@router.post("/login")
def login_user(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail = "User Not Found"
        )
    
    if not verify_password(
        user.password,
        db_user.hash_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )
    
    token = create_access_token(
        {"sub":db_user.email}
    )

    return{
        "access_token":token,
        "token_type":"bearer"
    }