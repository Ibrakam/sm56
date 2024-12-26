from fastapi import APIRouter, UploadFile, File
import random


photo_router = APIRouter(prefix='/photo', tags=['Фото'])


@photo_router.post('/save_photo')
async def save_photo_api(post_id: int, photo_file: UploadFile = File(...)):
    file_id = random.randint(1, 1_000_000)
    if photo_file:
        with open(f'db/images/photo_{file_id}_{post_id}.jpg', 'wb') as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)
            return {'status': 1, "message": "Успешно сохранено"}
    return {'status': 0, "message": "Error"}
