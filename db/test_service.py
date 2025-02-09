from db import get_db
from db.models import Question, Result


# Функция для добавления вопроса
def add_question_db(question_text, level, v1, v2, v3, v4, correct_answer):
    db = next(get_db())
    new_question = Question(question_text=question_text,
                            level=level,
                            v1=v1, v2=v2, v3=v3, v4=v4,
                            correct_answer=correct_answer)
    db.add(new_question)
    db.commit()
    return True


# Функция для получения 20 вопросов
def get_20_questions():
    db = next(get_db())
    all_questions = db.query(Question).all()
    return all_questions[:20]


# Функция для получения топ 10 пользователей
def get_top_10_users_db():
    db = next(get_db())
    top_10_users = db.query(Result.user_id).order_by(Result.correct_answers.desc())
    return top_10_users[:10]