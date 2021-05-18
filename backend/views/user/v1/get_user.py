from models.user_model import UserListModel
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Response, Depends
from utils.token_functions import get_current_active_user


router = APIRouter()


@router.get("/get/",
            responses={200: {"model": UserListModel},
                       400: {"description": "Bad Request Please check data."},
                       422: {"description": "RESPONSE NOT USED"},
                       500: {"description": "Internal Server Error"}})
def get_user(response: Response, current_user: UserListModel = Depends(get_current_active_user)):
    return current_user
