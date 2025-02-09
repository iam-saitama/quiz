from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Тип БД
SQL_DATABASE_URI ="sqlite:///quiz.db"

# Движок для БД
engine = create_engine(SQL_DATABASE_URI)

# Сессия для хранения данных
SessionLocal = sessionmaker(bind=engine)

# Полноценная БД
Base = declarative_base()

# Функция для подключения к БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()