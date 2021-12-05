from pydantic import BaseModel
from typing import Optional
from pydantic import Field, EmailStr
from datetime import datetime


class UserBaseModel(BaseModel):
    username: Optional[str] = Field(None, max_length=50)
    name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    email: EmailStr
    create_date: Optional[datetime]
    avatar: Optional[str] = None
    slug: Optional[str]
    bio: Optional[str]
    job: Optional[str]


class UserListModel(UserBaseModel):
    id: str = Field("", alias="_id")
    access_level: int
    disabled: bool = False


class RegisterUser(UserBaseModel):
    password: str


class UpdateUserModel(BaseModel):
    username: Optional[str] = Field(None, max_length=50)
    name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    slug: Optional[str] = Field(None, max_length=50)
    bio: Optional[str] = Field(None, max_length=50)
    job: Optional[str] = Field(None, max_length=50)


class LoginUserModel(BaseModel):
    email: EmailStr
    password: str


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
