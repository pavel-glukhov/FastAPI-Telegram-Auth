import os
from dataclasses import dataclass

from dotenv import load_dotenv
from starlette.templating import Jinja2Templates

root_path = os.path.dirname(os.path.dirname(__file__))
dotenv_path = os.path.join(root_path, '.env')
load_dotenv(dotenv_path)

templates = Jinja2Templates(directory=os.path.join(root_path, "templates"))


@dataclass
class BotConfig:
    telegram_token: str
    telegram_login: str


@dataclass
class AppConfig:
    bot: BotConfig
    domain_name: str


def load_config():
    """
    Main configuration of application.
    """
    return AppConfig(
        bot=BotConfig(
            telegram_token=os.getenv('TELEGRAM_TOKEN'),
            telegram_login=os.getenv('TELEGRAM_LOGIN'),
        ),
        domain_name=os.getenv('DOMAIN_NAME'),
    )
