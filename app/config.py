import os
from dataclasses import dataclass


@dataclass
class BotConfig:
    telegram_token: str
    telegram_login: str


@dataclass
class AppConfig:
    bot: BotConfig


def load_config():
    """
    Main configuration of application.
    """
    return AppConfig(
        bot=BotConfig(
            telegram_token=os.environ.get('TELEGRAM_TOKEN'),
            telegram_login=os.environ.get('TELEGRAM_LOGIN'),
        ),
    )
