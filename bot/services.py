from aiogram import Bot, Dispatcher
from app.config import AppConfig

class BotService:
    def __init__(
            self,
            config: AppConfig
    ):
        self.bot = Bot()
        self.dp = Dispatcher()
