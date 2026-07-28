from passlib.context import CryptContext  # type: ignore[import]

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str):
    print("Password:",password)
    print("Length:",len(password))
    return pwd_context.hash(password)

def verify_password(
        plain_password,
        hashed_password
):
    print("PLAIN PASSWORD:", plain_password)
    print("PLAIN LENGTH:", len(plain_password))
    return pwd_context.verify(
        plain_password,
        hashed_password
    )
