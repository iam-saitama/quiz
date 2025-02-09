from fastapi import APIRouter
from db.test_service import *


test_router = APIRouter(prefix="/tests", tags=["Вопросы"])


# Endpoint для добавления вопросов
@test_router.post("/add_question")
async def add_question(question_text, level, v1, v2, v3, v4, correct_answer):
    result = add_question_db(question_text=question_text,
                             level=level,
                             v1=v1, v2=v2, v3=v3, v4=v4,
                             correct_answer=correct_answer)
    return {"status": 1, "message": result}


# Endpoint для получения вопросов
@test_router.get("/get_questions")
async def get_questions():
    result = get_20_questions()
    return {"status": 1, "message": result}


# Endpoint для получения результатов
@test_router.get("/result")
async def get_results():
    result = get_top_10_users_db()
    user_result = [{"user_id": i[0]} for i in result]
    return {"status": 1, "message": user_result}