from typing import Optional
from models.user_model import UserListModel, UserAccessLevelRatio
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Response, Depends
from database.user.user_functions import UserDB
from configs.config import DATABASE_NAME, COLLECTION_NAME_USER
from utils.token_functions import is_active_user_admin
from database.pipeline_generator import user_access_level_ratio_pipeline


router = APIRouter()


@router.get("/statistic/access_level_ratio/",
            responses={200: {"model": UserAccessLevelRatio},
                       400: {"description": "Bad Request Please check data."},
                       422: {"description": "RESPONSE NOT USED"},
                       500: {"description": "Internal Server Error"}})
def user_access_level_ratio(
        response: Response, current_user: UserListModel = Depends(is_active_user_admin)):
    client = UserDB(database=DATABASE_NAME, collection=COLLECTION_NAME_USER)
    pipeline = user_access_level_ratio_pipeline()
    result = client.aggregate(pipeline)

    access_ratio = list(result)
    if not access_ratio:
        return Response(status_code=204)
    return JSONResponse(content=jsonable_encoder(access_ratio))
