from fastapi.exceptions import HTTPException
from models.user_model import UserListModel
from starlette.responses import JSONResponse
from fastapi import APIRouter, Response, status, Depends, UploadFile, File
import random
from database.user.user_functions import UserDB
from configs.config import DATABASE_NAME, COLLECTION_NAME_USER
from utils.token_functions import get_current_active_user
import os
from utils.common_functions import create_dir

router = APIRouter()
CURRENT_FILE_PATH = os.getcwd()

STATIC_AVATARS_FOLDER = os.path.join("static", "avatars")


@router.post("/change_avatar/", status_code=200, response_model_exclude_defaults=True,
             responses={200: {"description": "Successfully Changed"},
                        400: {"description": "Bad Request Please check data."},
                        422: {"description": "RESPONSE NOT USED"},
                        500: {"description": "Internal Server Error"}})
def change_avatar(response: Response, uploaded_file: UploadFile = File(...),
                  current_user: UserListModel = Depends(get_current_active_user)):
    client = UserDB(database=DATABASE_NAME, collection=COLLECTION_NAME_USER)
    file_name = f'{random.randint(0, 9999)}-{uploaded_file.filename.replace(" ", "-")}'
    file_location = os.path.join(CURRENT_FILE_PATH, STATIC_AVATARS_FOLDER, current_user.email)

    create_res = create_dir(file_location)
    if not create_res:
        return Response(status_code=500)

    file_full_location = os.path.join(file_location, file_name)

    with open(file_full_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())

    database_avatar_path = os.path.join(STATIC_AVATARS_FOLDER, current_user.email, file_name)
    result = client.update_one(current_user.email, {"avatar": database_avatar_path})
    if result:
        return Response(status_code=200)
    return HTTPException(status_code=500, detail="Update Job Has been Failed")
