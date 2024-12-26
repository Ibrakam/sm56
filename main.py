from fastapi import FastAPI
from db import Base, engine
from api.users import user_router
from api.photos import photo_router

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(photo_router)




