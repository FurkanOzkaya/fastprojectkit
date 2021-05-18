from fastapi.exceptions import HTTPException
from models.user_model import PasswordChangeModel, UserListModel
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Response, Depends, status
from database.user.user_functions import UserDB
from fastapi.encoders import jsonable_encoder
from configs.config import DATABASE_NAME, COLLECTION_NAME_USER
from utils.token_functions import get_current_active_user
from utils.common_functions import is_user_admin

router = APIRouter()


@router.patch("/password_change/",
              responses={200: {"description": "Successfully Changed"},
                         400: {"description": "Bad Request Please check data."},
                         422: {"description": "RESPONSE NOT USED"},
                         500: {"description": "Internal Server Error"}})
def password_change(response: Response, data: PasswordChangeModel,
                    current_user: UserListModel = Depends(get_current_active_user)):
    client = UserDB(database=DATABASE_NAME, collection=COLLECTION_NAME_USER)
    data = jsonable_encoder(data)
    result = client.update_password(current_user.email, data)
    if not result:
        return HTTPException(status_code=500, detail="Password Update Job has been Failed.")

    return JSONResponse(status_code=status.HTTP_200_CREATED, content={"status": "Successfully Changed."})
