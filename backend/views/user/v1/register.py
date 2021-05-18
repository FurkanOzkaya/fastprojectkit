from fastapi.exceptions import HTTPException
from starlette.responses import JSONResponse
from models.user_model import RegisterUser
from fastapi import APIRouter, Response, status
from database.user.user_functions import UserDB
from fastapi.encoders import jsonable_encoder
from configs.config import DATABASE_NAME, COLLECTION_NAME_USER
from datetime import datetime, date
router = APIRouter()


@router.post("/register/", status_code=201, response_model_exclude_defaults=True,
             responses={201: {"description": "Successfully Registered"},
                        400: {"description": "Bad Request Please check data."},
                        422: {"description": "RESPONSE NOT USED"},
                        500: {"description": "Internal Server Error"}})
def register(user: RegisterUser, response: Response):
    client = UserDB(database=DATABASE_NAME, collection=COLLECTION_NAME_USER)
    is_email_exist = client.get_user_with_email(user.email)
    if is_email_exist:
        return HTTPException(status_code=400, detail="Email Already Taken")
    request_body = jsonable_encoder(user)
    # For Normal users access_level will assign as 0
    request_body["access_level"] = 0
    # First opening active user
    request_body["disabled"] = False
    request_body["create_date"] = datetime.today()
    request_body["create_time"] = datetime.now()
    result = client.insert_one(request_body)
    if not result.inserted_id:
        return HTTPException(status_code=500, detail="Register Job has been Failed.")

    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"status": "Successfully Registered."})
