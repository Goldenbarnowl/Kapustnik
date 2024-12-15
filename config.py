from aiogram import Bot
from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties
from supabase import Client, create_client
from pydantic_settings import BaseSettings


class Secrets(BaseSettings):
    token: str
    supabase_url: str
    supabase_key: str
    admin_id: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


secrets = Secrets()

url: str = secrets.supabase_url
key: str = secrets.supabase_key
supabase: Client = create_client(url, key)


default = DefaultBotProperties(parse_mode='HTML', protect_content=False)
bot = Bot(token=secrets.token, default=default)
dp = Dispatcher()
