from fastapi import FastAPI
from api.users import user_router
from api.tests import test_router
from db import engine, Base

# Для создания БД
Base.metadata.create_all(engine)

app = FastAPI(docs_url="/")

app.include_router(user_router)
app.include_router(test_router)
