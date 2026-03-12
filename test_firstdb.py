import pytest
import uuid
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Строка подключения к локальной БД (замените при необходимости)
DB_URL = "postgresql://myuser:mypassword@localhost:5432/firstdb"

# Базовый класс моделей
Base = declarative_base()

# Модель таблицы subject (другие таблицы не требуются для тестов)
class Subject(Base):
    __tablename__ = 'subject'
    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String)

# Фикстура для создания сессии БД
@pytest.fixture(scope='function')
def db_session():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_add_subject(db_session):
    """Тест добавления нового предмета."""
    # Генерируем уникальное название, чтобы избежать конфликтов
    unique_title = f"Test Subject {uuid.uuid4()}"
    subject = Subject(subject_title=unique_title)

    db_session.add(subject)
    db_session.commit()
    subject_id = subject.subject_id

    try:
        # Проверяем, что запись появилась в БД
        fetched = db_session.get(Subject, subject_id)
        assert fetched is not None
        assert fetched.subject_title == unique_title
    finally:
        # Удаляем созданную запись (если она существует)
        obj = db_session.get(Subject, subject_id)
        if obj:
            db_session.delete(obj)
            db_session.commit()

def test_update_subject(db_session):
    """Тест изменения названия предмета."""
    # Создаём предмет
    unique_title = f"Test Subject {uuid.uuid4()}"
    subject = Subject(subject_title=unique_title)
    db_session.add(subject)
    db_session.commit()
    subject_id = subject.subject_id

    try:
        # Обновляем название
        new_title = f"Updated {unique_title}"
        subject.subject_title = new_title
        db_session.commit()

        # Проверяем, что изменения применились
        updated = db_session.get(Subject, subject_id)
        assert updated.subject_title == new_title
    finally:
        # Удаляем созданную запись
        obj = db_session.get(Subject, subject_id)
        if obj:
            db_session.delete(obj)
            db_session.commit()

def test_delete_subject(db_session):
    """Тест удаления предмета."""
    # Создаём предмет
    unique_title = f"Test Subject {uuid.uuid4()}"
    subject = Subject(subject_title=unique_title)
    db_session.add(subject)
    db_session.commit()
    subject_id = subject.subject_id

    try:
        # Удаляем его
        db_session.delete(subject)
        db_session.commit()

        # Проверяем, что запись больше не существует
        deleted = db_session.get(Subject, subject_id)
        assert deleted is None
    finally:
        # Дополнительная очистка на случай, если удаление не произошло из-за ошибки
        obj = db_session.get(Subject, subject_id)
        if obj:
            db_session.delete(obj)
            db_session.commit()