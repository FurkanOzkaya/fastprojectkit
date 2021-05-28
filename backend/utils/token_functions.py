from typing import Optional
from database.user.user_functions import UserDB
from configs.config import DATABASE_NAME, COLLECTION_NAME_USER, SECRET_KEY, JWT_ALGORITHM, ADMIN_ACCESS_LEVEL
from fastapi.security import OAuth2PasswordBearer
from utils.common_functions import verify_password, handle_id_for_user_model
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends, Header
from models.user_model import UserListModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticate_user(email: str, password: str):
    client = UserDB(database=DATABASE_NAME, collection=COLLECTION_NAME_USER)
    user = client.get_user_with_email_include_password(email)
    user = handle_id_for_user_model(user)
    if not user:
        return False
    if not verify_password(password, user['password']):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Header(None)):
    client = UserDB(database=DATABASE_NAME, collection=COLLECTION_NAME_USER)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
        object_id: str = payload.get("_id", None)
        if object_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = client.get_user_with_object_id(object_id=object_id)
    print(user, "asdasqweqweqweqweqwe")
    if user is None:
        raise credentials_exception

    user = handle_id_for_user_model(user)
    user = UserListModel(**user)
    return user


async def get_current_active_user(current_user: UserListModel = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


async def is_active_user_admin(current_user: UserListModel = Depends(get_current_active_user)):
    if current_user.access_level == ADMIN_ACCESS_LEVEL:
        return current_user
    else:
        raise HTTPException(status_code=401, detail="User is not Admin")
