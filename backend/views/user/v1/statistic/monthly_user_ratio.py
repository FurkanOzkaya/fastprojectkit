from typing import Optional
from models.user_model import UserListModel, MonthlyUserRatio
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Response, Depends
from database.user.user_functions import UserDB
from configs.config import DATABASE_NAME, COLLECTION_NAME_USER
from utils.token_functions import is_active_user_admin
from database.pipeline_generator import get_user_count
import calendar
from datetime import date, datetime
router = APIRouter()


def prepare_dates(first, last, month, year):
    if first == 0:
        first += 1
    start_date = datetime.strptime(f"{first}-{month}-{year}", '%d-%m-%Y')
    end_date = datetime.strptime(f"{last}-{month}-{year}", '%d-%m-%Y')
    return start_date, end_date


@router.get("/statistic/monthly_user_ratio/",
            responses={200: {"model": MonthlyUserRatio},
                       400: {"description": "Bad Request Please check data."},
                       422: {"description": "RESPONSE NOT USED"},
                       500: {"description": "Internal Server Error"}})
def monthly_user_ratio(
        response: Response, current_user: UserListModel = Depends(is_active_user_admin)):
    client = UserDB(database=DATABASE_NAME, collection=COLLECTION_NAME_USER)
    year = date.today().year
    result_statistic = {}
    for month in range(1, 13):
        first, last = calendar.monthrange(year, month)
        start_date, end_date = prepare_dates(first, last, month, year)
        pipeline = get_user_count(start_date, end_date)
        result = client.aggregate(pipeline)
        result = list(result)
        count = 0
        if result:
            count = result[0]['count']
        result_statistic.update({calendar.month_name[month]: count})

    if not result_statistic:
        return Response(status_code=204)
    return JSONResponse(content=jsonable_encoder(result_statistic))
