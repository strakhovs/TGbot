import os

from dotenv import load_dotenv
from pydantic import BaseSettings, SecretStr, StrictStr

load_dotenv()


class BotSettings(BaseSettings):
    bot_token: SecretStr = os.getenv("BOT_TOKEN", None)
