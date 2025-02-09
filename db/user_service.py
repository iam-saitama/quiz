from db import get_db
from db.models import User, Question, UserAnswer, Result


# Функция для добавления пользователя
def add_user_db(username, phone_number, level=None):
    db = next(get_db())
    new_user = User(username=username,
                    phone_number=phone_number,
                    level=level)
    db.add(new_user)
    db.commit()
    return True


# Функция для получения всех пользователей
def get_all_users_db():
    db = next(get_db())
    all_users = db.query(User).all()
    return all_users


# Функция для получения определенного пользователя
def get_exact_user_db(user_id):
    db = next(get_db())
    exact_user = db.query(User).filter_by(id=user_id).first()
    if exact_user:
        return exact_user
    return False


# Функция для сохранения ответа пользователя
def user_answer_db(user_id, q_id, user_answer, level):
    db = next(get_db())
    exact_question = db.query(Question).filter_by(id=q_id).first()
    if exact_question:
        if exact_question.correct_answer == user_answer:
            correctness = True
        else:
            correctness = False

        new_user_answer = UserAnswer(user_id=user_id,
                                     question_id=q_id,
                                     answer=user_answer,
                                     level=level,
                                     correctness=correctness)
        db.add(new_user_answer)
        db.commit()
        if correctness:
            user_result = db.query(Result).filter_by(user_id=user_id).first()
            if user_result:
                user_result.correct_answers += 1
                db.commit()
                return True
            return False

    return False


# Получаем результат пользователя
def get_user_result_db(user_id):
    db = next(get_db())
    user_result = db.query(Result).filter_by(user_id=user_id).first()
    if user_result:
        return user_result
    return False
