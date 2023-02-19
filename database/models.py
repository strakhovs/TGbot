from datetime import datetime
import peewee

db = peewee.SqliteDatabase('bot.db')


class ModelBase(peewee.Model):
    """
    Базовый класс для таблиц
    """
    class Meta:
        database = db


class ChatHistory(ModelBase):
    """
    Таблица истории чата
    """
    created_at = peewee.DateTimeField(default=datetime.now())
    person_id = peewee.IntegerField(null=False)
    message = peewee.CharField()


class ResponseHistory(ModelBase):
    """
    Таблица истории запросов
    """
    person_id = peewee.IntegerField()
    response = peewee.CharField()


class User(ModelBase):
    """
    Таблица пользователей
    """
    person_id = peewee.IntegerField(unique=True)
    name = peewee.CharField(max_length=25)
    region = peewee.CharField(max_length=5, default='RU')
    currency = peewee.CharField(max_length=5, default='RUB')
