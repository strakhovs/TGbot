import os
from loguru import logger
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    logger.exception('Не найден файл .env')
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()
    logger.debug('Переменные окружения загружены')

BOT_TOKEN = os.getenv("BOT_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("low", "Поиск по мин. ценам"),
    ("high", "Поиск по макс. ценам"),
    ("custom", "Поиск в диапазоне цен"),
    ("history", "История запросов"),
    ("edit", "Редактирование профиля")
)
