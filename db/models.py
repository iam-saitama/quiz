from sqlalchemy import (Column, String, Integer, Boolean, DateTime, ForeignKey)
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime


# Создаем модель User
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(52), nullable=False)
    phone_number = Column(String, nullable=False)
    level = Column(String, default="Select your level")
    reg_date = Column(DateTime, default=datetime.now())


# Модель вопроса
class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_text = Column(String, nullable=False)
    v1 = Column(String)
    v2 = Column(String)
    v3 = Column(String)
    v4 = Column(String)
    correct_answer = Column(String, nullable=False)
    level = Column(String, default="easy")


# Модель ответа пользователя
class UserAnswer(Base):
    __tablename__ = "user_answers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    answer = Column(String)
    correctness = Column(Boolean, default=False)
    level = Column(String, ForeignKey="users.level")

    user_fk = relationship(User, lazy="subquery")
    question_fk = relationship(Question, lazy="subquery")


# Модель Result
class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    correct_answers = Column(Integer, default=0)
    level = Column(String, ForeignKey="users.level")

    user_fk = relationship(User, lazy="subquery")
