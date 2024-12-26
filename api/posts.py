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

# Endpoint для получние всех постов
# Endpoint для получние определенного поста
# Endpoint для изменения поста
# Endpoint для удаления поста


