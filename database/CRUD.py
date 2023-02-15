from datetime import datetime
from telebot.types import Message
from .models import db, ChatHistory, ResponseHistory


def store_message(message: Message) -> None:
    with db.atomic():
        ChatHistory.create(created_at=datetime.now(),
                           person_id=int(message.from_user.id),
                           message=message.text)


def store_response(person_id: int, response_string: str) -> None:
    with db.atomic():
        ResponseHistory.create(person_id=person_id, response=response_string)


def get_history(person_id: int):
    query = ResponseHistory.select(ResponseHistory.response).\
        where(ResponseHistory.person_id == person_id).\
        limit(10).\
        order_by(ResponseHistory.id.desc())
    responses_selected = query.dicts().execute()
    return responses_selected


def create_tables():
    with db:
        db.create_tables([ResponseHistory])


db.connect()
