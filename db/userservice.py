from db import get_db
from db.models import User


# Функция для регистрации
def register_user_db(username, phone_number, email,
                     password, name, surname=None, age=None, city=None):
    db = next(get_db())
    new_user = User(username=username, phone_number=phone_number,
                    email=email, password=password, name=name,
                    surname=surname, age=age, city=city)
    db.add(new_user)
    db.commit()
    return True


# Функция для получение определенного пользователя или всех
def get_exact_or_all_user(user_id=0):
    db = next(get_db())
    if user_id == 0:
        all_users = db.query(User).all()
        return all_users
    exact_user = db.query(User).filter_by(id=user_id).first()
    return exact_user


# Функция для изменения пользователя
def update_user_db(user_id, change_info, new_info):
    db = next(get_db())
    update_user = db.query(User).filter_by(id=user_id).first()
    if update_user:
        if change_info == "username":
            update_user.username = new_info
        elif change_info == "email":
            update_user.email = new_info
        elif change_info == "password":
            update_user.password = new_info
        elif change_info == "phone_number":
            update_user.phone_number = new_info
        elif change_info == "name":
            update_user.name = new_info
        elif change_info == "surname":
            update_user.surname = new_info
        elif change_info == "age":
            update_user.age = new_info
        elif change_info == "city":
            update_user.city = new_info
        else:
            return False
        db.commit()
        return True
    return False


# Функция для удаления
def delete_user_db(user_id):
    db = next(get_db())
    delete_user = db.query(User).filter_by(id=user_id).first()
    if delete_user:
        db.delete(delete_user)
        db.commit()
        return True
    return False

