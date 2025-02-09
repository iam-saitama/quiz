from fastapi import APIRouter
from db.user_service import *


user_router = APIRouter(prefix="/users", tags=["Пользователи"])


# Endpoint для добавления пользователя
@user_router.post("/add_users")
async def add_user(username: str, phone_number: str, level: str = None):
    result = add_user_db(username=username,
                         phone_number=phone_number,
                         level=level)
    return {"status": 1, "message": result}


# Endpoint для получения всех пользователей
@user_router.get("/get_all_users")
async def get_all_users():
    result = get_all_users_db()
    return {"status": 1, "message": result}


# Endpoint для получения определенного пользователя
@user_router.get("/get_exact_user")
async def get_exact_user(user_id: int):
    result = get_exact_user_db(user_id)
    if result:
        return {"status": 1, "message": result}
    return {"status": 0, "message": result}


# Endpoint для сохранения ответа пользователя
@user_router.post("/save_user_answer")
async def save_user_answer(user_id: int, q_id: int,
                           user_answer: str):
    result = user_answer_db(user_id=user_id,
                            q_id=q_id,
                            user_answer=user_answer)
    if result:
        return {"status": 1, "message": result}
    return {"status": 0, "message": result}


# Endpoint для получения результата определенного пользователя
@user_router.get("/get_user_result")
async def get_user_result(user_id: int):
    result = get_user_result_db(user_id)
    if result:
        return {"status": 1, "message": result}
    return {"status": 0, "message": result}
