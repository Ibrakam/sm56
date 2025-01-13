from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from db import Base, engine
from api.users import user_router
from api.photos import photo_router
from api.posts import post_router
from api.hashtags import hashtag_route
from api.comments import comment_route
from fastapi.templating import Jinja2Templates

from db.userservice import get_exact_or_all_user

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/docs')
templates = Jinja2Templates(directory="templates")

app.include_router(user_router)
app.include_router(photo_router)
app.include_router(post_router)
app.include_router(comment_route)
app.include_router(hashtag_route)


@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    users = get_exact_or_all_user(user_id=0)
    return templates.TemplateResponse(name="index.html", request=request, context={"users": users})


@app.get("/all_users", response_class=HTMLResponse)
async def main(request: Request):
    users = get_exact_or_all_user(user_id=0)
    return templates.TemplateResponse(name="users.html", request=request, context={"users": users})


@app.get("/get_exact_user/{id}", response_class=HTMLResponse)
async def main(request: Request, id: int):
    user = get_exact_or_all_user(user_id=id)
    return templates.TemplateResponse(name="exact_user.html", request=request, context={"user": user})


@app.get("/update_user", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(name="update.html", request=request)