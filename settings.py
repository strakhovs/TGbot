import os

from dotenv import load_dotenv
from pydantic import BaseSettings, SecretStr, StrictStr

load_dotenv()


class BotSettings(BaseSettings):
    bot_token: SecretStr = os.getenv("BOT_TOKEN", None)


class SiteSettings(BaseSettings):
    site_key: SecretStr = os.getenv("SITE_KEY", None)
    site_host: StrictStr = os.getenv("SITE_HOST", None)
