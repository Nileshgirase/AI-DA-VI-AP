
from fastapi import Depends, HTTPException # type: ignore[reportMissingImports]

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials # type: ignore[reportMissingImports]

from app.utils.jwt_handler import verify_token

security = HTTPBearer()

def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),

):
    print("Credentials:", credentials)
    print("Token:", credentials.credentials)

    token = credentials.credentials

    payload = verify_token(token)
    
    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )
    
    email = payload.get("sub")

    if email is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token payload"
        )
    
    return payload