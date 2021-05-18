from fastapi.exceptions import HTTPException
from models.user_model import UserListModel, UpdateUserModel
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Response, Depends, status
from database.user.user_functions import UserDB
from fastapi.encoders import jsonable_encoder
from configs.config import DATABASE_NAME, COLLECTION_NAME_USER
from utils.token_functions import get_current_active_user
from utils.common_functions import is_user_admin

router = APIRouter()


@router.patch("/update/",
              responses={200: {"model": UserListModel},
                         400: {"description": "Bad Request Please check data."},
                         422: {"description": "RESPONSE NOT USED"},
                         500: {"description": "Internal Server Error"}})
def update_user(response: Response, data: UpdateUserModel, current_user: UserListModel = Depends(get_current_active_user)):
    client = UserDB(database=DATABASE_NAME, collection=COLLECTION_NAME_USER)
    # check if username change if change username exist or not control
    if not is_user_admin(current_user):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User is not Admin",
            headers={"WWW-Authenticate": "Bearer"},
        )
    print(f"second  data ==> {data}")
    data = jsonable_encoder(data)
    result = client.update_one(current_user.email, data)

    if result:
        user = client.get_user_with_email(email=current_user.email)
        return JSONResponse(content=user)
    return HTTPException(status_code=500, detail="Update Job Has been Failed")
