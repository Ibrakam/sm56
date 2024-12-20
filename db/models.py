from db import Base
from sqlalchemy import (Column, Integer,
                        String, Boolean, ForeignKey, DateTime, Text)
from sqlalchemy.orm import relationship
from datetime import datetime


# Модель пользователя
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=True)
    phone_number = Column(String, nullable=False, unique=True)
    age = Column(String, nullable=True)
    city = Column(String, nullable=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())


# Модель хэштег
class Hashtag(Base):
    __tablename__ = 'hashtags'

    id = Column(Integer, autoincrement=True, primary_key=True)
    text = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())


# Модель постов
class UserPost(Base):
    __tablename__ = 'userposts'

    id = Column(Integer, autoincrement=True, primary_key=True)
    location = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    main_text = Column(Text, nullable=False)
    hashtag = Column(String, ForeignKey('hashtags.text'))
    reg_date = Column(DateTime, default=datetime.now())

    user_fk = relationship(User, lazy='subquery')
    hashtag_fk = relationship(Hashtag, lazy='subquery')


# Модель фото
class PostPhoto(Base):
    __tablename__ = 'photos'

    id = Column(Integer, autoincrement=True, primary_key=True)
    post_id = Column(Integer, ForeignKey('userposts.id'))
    photo_file = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())

    post_fk = relationship(UserPost, lazy='subquery')


# Модель коммент
class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, autoincrement=True, primary_key=True) #1
    user_id = Column(Integer, ForeignKey('users.id')) #2
    post_id = Column(Integer, ForeignKey('userposts.id')) #3
    text = Column(String, nullable=False) #wewrew
    reg_date = Column(DateTime, default=datetime.now()) #12.12.12

    user_fk = relationship(User, lazy='subquery') # {name: sdfsd, phone: 123123}
    post_fk = relationship(UserPost, lazy='subquery')
