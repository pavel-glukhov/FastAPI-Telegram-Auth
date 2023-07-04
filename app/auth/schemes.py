from typing import Optional

from pydantic import BaseModel


class TelegramAuth(BaseModel):
    id: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    photo_url: Optional[str]
    auth_date: Optional[str]
    hash: Optional[str]
