from db import get_db
from db.models import PostPhoto, UserPost, Comment, Hashtag

"""
UserPost functions
"""


# Cоздания поста
def add_post_db(user_id, main_text, location, hashtag):
    db = next(get_db())
    new_post = UserPost(user_id=user_id, main_text=main_text,
                        location=location, hashtag=hashtag)
    db.add(new_post)
    db.commit()
    return True


# Изменения поста
def change_post_db(post_id, change_info, new_info):
    db = next(get_db())
    update_post = db.query(UserPost).filter_by(id=post_id).first()
    if update_post:
        if change_info == 'location':
            update_post.location = new_info
        elif change_info == 'text':
            update_post.main_text = new_info
        elif change_info == 'hashtag':
            update_post.hashtag = new_info
        else:
            return False
        db.commit()
        return True
    return False


def delete_post_db(post_id):
    db = next(get_db())
    post_to_delete = db.query(PostPhoto).filter_by(id=post_id).first()
    if post_to_delete:
        db.delete(post_to_delete)
        return True
    return False


# получ всех постов


def get_all_posts_db():
    db = next(get_db())
    all_posts = db.query(UserPost).all()
    return all_posts


# ПОлучение определенного поста

def get_exact_post_db(post_id):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(id=post_id).first()
    return exact_post


"""
Comment functions
"""
"""
Comment functions
"""


# Создание коммента
def create_comment_db(user_id, post_id, text, reg_date):
    db = next(get_db())
    new_comment = Comment(user_id=user_id, post_id=post_id, text=text, reg_date=reg_date)
    db.add(new_comment)
    db.commit()
    return True


# Полчение коммента по его айди
def get_exact_comment_db(comment_id):
    db = next(get_db())
    exact_comment = db.query(Comment).filter_by(id=comment_id).first()
    return exact_comment


# Получение всех комментов по айди поста
def get_all_comments_db(post_id):
    db = next(get_db())
    all_comments = db.query(Comment).filter_by(post_id=post_id).all()
    return all_comments


# Изменение коммента
def edit_comment_db(comment_id, new_text):
    db = next(get_db())
    edit_comment = db.query(Comment).filter_by(id=comment_id).first()
    if edit_comment is None:
        return False
    edit_comment.text = new_text
    db.commit()
    return True


# Удаление коммента
def delete_comment_db(comment_id):
    db = next(get_db())
    delete_comment = db.query(Comment).filter_by(id=comment_id).first()
    if delete_comment:
        db.delete(delete_comment)
        db.commit()
        return True
    return False


"""
Hashtag functions
"""


# Создание хэштега
def create_hashtag_db(text):
    db = next(get_db())
    db.add(Hashtag(text=text))
    db.commit()
    return True
# Получение хэштега по названию

# Получение всех хэштегов
# Удаление хэштега
# Изменение хэштега
