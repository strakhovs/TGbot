from datetime import datetime
from telebot.types import Message
from loguru import logger
from .models import db, ChatHistory, ResponseHistory, User
from typing import Iterable, Optional


def store_message(message: Message) -> None:
    """
    Сохраняет сообщения в БД
    """
    with db.atomic():
        ChatHistory.create(created_at=datetime.now(),
                           person_id=int(message.from_user.id),
                           message=message.text)
        logger.debug(f'Сообщение "{message.text}" отправлено в базу данных')


def store_response(person_id: int, response_string: str) -> None:
    """
    Сохраняет результаты запросов в БД
    """
    with db.atomic():
        ResponseHistory.create(person_id=person_id, response=response_string)
        logger.debug('Результаты запроса отправлены в базу данных')


def get_history(person_id: int) -> Iterable:
    """
    Запрос истории из БД
    """
    query = ResponseHistory.select(ResponseHistory.response).\
        where(ResponseHistory.person_id == person_id).\
        limit(10).\
        order_by(ResponseHistory.id.desc())
    responses_selected = query.dicts().execute()
    return responses_selected


def get_user(person_id: int) -> Optional[User]:
    """
    Запрос данных пользователя из БД
    """
    try:
        user = User.get(User.person_id == person_id)
    except User.DoesNotExist:
        logger.debug('Пользователь не найден')
        return None
    return user


def create_tables() -> None:
    """
    Создание таблиц в БД
    """
    with db:
        db.create_tables([ChatHistory, ResponseHistory, User])
        logger.debug('Таблицы созданы')


db.connect()
create_tables()
