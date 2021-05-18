from pydantic import BaseModel
from typing import Optional
from pydantic import Field, EmailStr
from datetime import datetime, date


class UserBaseModel(BaseModel):
    username: Optional[str]
    name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    email: EmailStr
    create_date: Optional[date]
    create_time: Optional[datetime]


class UserListModel(UserBaseModel):
    access_level: int
    disabled: bool = False


class RegisterUser(UserBaseModel):
    password: str


class UpdateUserModel(BaseModel):
    username: Optional[str]
    name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    disabled: Optional[bool] = False
    access_level: Optional[int]


class LoginUserModel(BaseModel):
    email: EmailStr
    password: str


class TokenData(BaseModel):
    email: Optional[str] = None


class PasswordChangeModel(BaseModel):
    password: str


class UserAccessLevelRatio(BaseModel):
    id: int = Field(alias="_id")
    count: int


class MonthlyUserRatio(BaseModel):
    January: int
    February: int
    March: int
    April: int
    May: int
    June: int
    July: int
    August: int
    September: int
    October: int
    November: int
    December: int
