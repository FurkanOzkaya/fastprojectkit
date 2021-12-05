from typing import Optional
from models.user_model import UserListModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Response, Depends
from database.user.user_functions import UserDB
from utils.token_functions import is_active_user_admin


router = APIRouter()


@router.get("/all/",
            responses={200: {"model": UserListModel},
                       400: {"description": "Bad Request Please check data."},
                       422: {"description": "RESPONSE NOT USED"},
                       500: {"description": "Internal Server Error"}})
def all_users_api(
        response: Response, current_user: UserListModel = Depends(is_active_user_admin),
        date: Optional[str] = None):
    client = UserDB()

    users = client.get_all_documents(date)

    all_users = list(users)
    if not all_users:
        return Response(status_code=204)
    return JSONResponse(content=jsonable_encoder(all_users))
