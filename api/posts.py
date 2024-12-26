from db.postservice import (add_post_db, get_exact_post_db,
                            get_all_posts_db, delete_post_db, change_post_db)
from fastapi import APIRouter
from api import result_message

post_router = APIRouter(prefix='/post', tags=['Посты'])


# Endpoint для добавления поста
@post_router.post('/add_post')
async def add_post(main_text: str, user_id: int,
                   location: str, hashtag: str):
    result = add_post_db(user_id=user_id,
                         main_text=main_text,
                         location=location,
                         hashtag=hashtag)
    return result_message(result)



@post_router.put('/change_post')
async def change_post(post_id: int, change_info: str, new_info: str):
    result = change_post_db(post_id=post_id, change_info=change_info, new_info=new_info)
    return result_message(result)


@post_router.delete('/delete_post')
async def delete_post(post_id: int):
    result = delete_post_db(post_id=post_id)
    return result_message(result)


@post_router.get('/get_all_posts')
async def get_all_posts():
    result = get_all_posts_db()
    return result_message(result)


@post_router.get('/get_exact_post')
async def get_exact_post(post_id: int):
    result = get_exact_post_db(post_id=post_id)
    return result_message(result)

