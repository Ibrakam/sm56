from fastapi import APIRouter
from api import result_message
from db.postservice import *

hashtag_route = APIRouter(prefix='/hashtag', tags=['/Хештеги'])


@hashtag_route.post('/create_hashtag')
async def create_hashtag(text: str):
    result = create_hashtag_db(text=text)
    return result_message(result)


@hashtag_route.get('/get_hashtag_by_name')
async def get_hashtag_by_name(text: str):
    result = get_hashtag_by_name_db(text)
    return result_message(result)


@hashtag_route.get('/get_all_hashtags')
async def get_all_hashtags():
    result = get_all_hashtags_db()
    return result_message(result)


# @hashtag_route.put('/update_hashtag')
# async def update_hashtag(hashtag_id: int, new_text: str):
#     result = update_hashtag_db(hashtag_id=hashtag_id, new_text=new_text)
#     return result_message(result)
