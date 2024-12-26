from fastapi import APIRouter
from pydantic import BaseModel

from api import result_message
from db.postservice import *

comment_route = APIRouter(prefix='/comment', tags=['/Комментарии'])


class CommentModel(BaseModel):
    user_id: int
    post_id: int
    text: str


@comment_route.post('/add_post')
async def add_post(user_data: CommentModel):
    comment_dict = dict(user_data)
    result = add_post_db(**comment_dict)
    return result_message(result)


@comment_route.put('/change_post')
async def change_post(post_id: int, change_info: str, new_info: str):
    result = change_post_db(post_id, change_info, new_info)
    return result_message(result)


@comment_route.delete('/delete_post')
async def delete_post(post_id: int):
    result = delete_comment_db(post_id)
    return result_message(result)


@comment_route.get('/get_all_posts')
async def get_all_posts(post_id: int):
    result = get_all_posts(post_id)
    return result_message(result)


@comment_route.get('/get_axact_post')
async def get_exact_post(post_id: int):
    result = get_exact_post(post_id)
    return result_message(result)
