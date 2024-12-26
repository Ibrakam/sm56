from fastapi import APIRouter
from db.userservice import *
from pydantic import BaseModel
from typing import Optional
from api import result_message
import re

user_router = APIRouter(prefix="/user", tags=['Пользователь'])

regex = re.compile(
    r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")


def check_email(email):
    if re.fullmatch(regex, email):
        return True
    return False


class UserModel(BaseModel):
    username: str
    phone_number: str
    email: str
    password: str
    name: str
    surname: Optional[str] = None
    age: Optional[str] = None
    city: Optional[str] = None


@user_router.post('/register_user')
async def register_user(user_data: UserModel):
    user_dict = dict(user_data)
    checker = check_email(user_data.email)
    if checker:
        result = register_user_db(**user_dict)
        return result_message(result)
    return "Неверный email"


@user_router.get('/get_exact_all_users')
async def get_users(user_id: int = 0):
    result = get_exact_or_all_user(user_id)
    return result_message(result)


@user_router.put('/update_user')
async def update_user(user_id: int, change_info: str,
                      new_info: str):
    result = update_user_db(user_id, change_info, new_info)
    return result_message(result)


@user_router.delete('/delete_user')
async def delete_user(user_id: int):
    result = delete_user_db(user_id)
    return result_message(result)
