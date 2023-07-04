import hashlib
import hmac
import time

from app.auth.exceptions import TelegramDataError, TelegramDataIsOutdated


def verify_telegram_authentication(telegram_bot_token: str,
                                   request_data: dict) -> dict:
    request_data = request_data.copy()
    """
    Checking authorization telegram data according to the information
    in telegram doc: https://core.telegram.org/widgets/login
    :param telegram_bot_token:
    :param request_data:
    :return:
    """
    received_hash = request_data.pop('hash', None)
    auth_date = request_data.get('auth_date')

    if _verify_telegram_session_outdate(auth_date):
        raise TelegramDataIsOutdated(
            'Telegram authentication session is expired.'
        )

    generated_hash = _generate_hash(request_data, telegram_bot_token)

    if generated_hash != received_hash:
        raise TelegramDataError(
            'Request data is incorrect'
        )

    return request_data


def _verify_telegram_session_outdate(auth_date: str) -> bool:
    one_day_in_second = 86400
    unix_time_now = int(time.time())
    unix_time_auth_date = int(auth_date)
    timedelta = unix_time_now - unix_time_auth_date

    if timedelta > one_day_in_second:
        return True
    return False


def _generate_hash(data: dict, token: str) -> str:
    request_data_alph_sorted = sorted(data.items(),
                                      key=lambda v: v[0])

    data_check_string = '\n'.join(f'{key}={value}' for key, value in
                                  request_data_alph_sorted)

    secret_key = hashlib.sha256(token.encode()).digest()
    generated_hash = hmac.new(
        key=secret_key,
        msg=data_check_string.encode(),
        digestmod=hashlib.sha256
    ).hexdigest()

    return generated_hash
