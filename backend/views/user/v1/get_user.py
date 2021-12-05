from utils.common_functions import handle_id_for_model
from starlette.responses import JSONResponse
from database.user.user_functions import UserDB
from models.user_model import UserListModel
from fastapi import APIRouter, Response, Depends
from utils.token_functions import get_current_active_user
router = APIRouter()


@router.get("/get/",
            responses={200: {"model": UserListModel},
                       400: {"description": "Bad Request Please check data."},
                       422: {"description": "RESPONSE NOT USED"},
                       500: {"description": "Internal Server Error"}})
def get_user(response: Response, current_user: UserListModel = Depends(get_current_active_user)):
    client = UserDB()

    user = client.get_user_with_email(current_user.email)
    user = handle_id_for_model(user)
    create_date = user["create_date"]
    create_date = create_date.strftime("%m/%d/%Y, %H:%M:%S")
    user["create_date"] = create_date
    return JSONResponse(content=user, status_code=200)
