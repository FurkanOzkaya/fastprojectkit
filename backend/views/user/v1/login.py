from configs.config import ACCESS_TOKEN_EXPIRE_MINUTES
from models.user_model import UserListModel
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Response, Depends, HTTPException, status
from models.user_model import LoginUserModel
from datetime import timedelta
from utils.token_functions import authenticate_user, create_access_token


router = APIRouter()


@router.post("/login/",
             responses={200: {"model": UserListModel},
                        400: {"description": "Bad Request Please check data."},
                        422: {"description": "RESPONSE NOT USED"},
                        500: {"description": "Internal Server Error"}})
def login(response: Response, login_user_model: LoginUserModel):
    user = authenticate_user(login_user_model.email, login_user_model.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data={"_id": user["_id"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
