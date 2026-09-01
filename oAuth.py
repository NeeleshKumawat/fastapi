from fastapi import FastAPI, HTTPException, Depends
from jose import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext

app = FastAPI()

SECRET_KEY = "mysecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# PASSWORD HASHING
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto", bcrypt__rounds=4)

# oauth Setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# dummy user Db - hash password at startup, not at module load
fake_users_db = {}

@app.on_event("startup")
async def startup_event():
    fake_users_db["admin"] = {
        "username": "admin",
        "hashed_password": pwd_context.hash("1234")
    }

# verify password
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def createToken(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({
        "exp": expire
    })

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return token


@app.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)

    if not user or not verify_password(form_data.password, user['hashed_password']):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password"
        )

    access_token = createToken({'sub': user['username']})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token has expired"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

@app.get('/secure')
def secure_data(user = Depends(verify_token)):
    return {
        "message": "Secure Data Accessed",
        "user": user
    }
