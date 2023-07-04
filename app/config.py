import os
from dataclasses import dataclass

from dotenv import load_dotenv
from starlette.templating import Jinja2Templates

ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
DOTENV_PATH = os.path.join(ROOT_PATH, '.env')
load_dotenv(DOTENV_PATH)

templates = Jinja2Templates(directory=os.path.join(ROOT_PATH, "templates"))


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
            telegram_token=os.getenv('TELEGRAM_TOKEN'),
            telegram_login=os.getenv('TELEGRAM_LOGIN'),
        ),
    )
