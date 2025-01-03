from fastapi import FastAPI
from db import Base, engine
from api.users import user_router
from api.photos import photo_router
from api.posts import post_router
from api.hashtags import hashtag_route
from api.comments import comment_route

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(photo_router)
app.include_router(post_router)
app.include_router(comment_route)
app.include_router(hashtag_route)




