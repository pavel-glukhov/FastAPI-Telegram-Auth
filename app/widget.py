from enum import Enum


class Size(Enum):
    """Button Size variants"""
    LARGE: str = 'large'
    MEDIUM: str = 'medium'
    SMALL: str = 'small'


class TelegramLoginWidget:
    """
    Class to generate Telegram login Widget according to the information
     from the official documentation: https://core.telegram.org/widgets/login
     
     Callback Telegram Login Widget is required:
     - telegram_login: str
     
     Additional params:
     - size: enum [Size.LARGE | Size.MEDIUM | Size.SMALL]
     - user_photo: bool
     - corner_radius: integer
     - access_write: bool
     
    Redirect Telegram Login Widget is required:
     - telegram_login: str
     - redirect_url : str
     
     Additional params:
     - size: enum [Size.LARGE | Size.MEDIUM | Size.SMALL]
     - user_photo: bool
     - corner_radius: integer
     - access_write: bool
     
    """

    def __init__(self, telegram_login: str,
                 size: Size = Size.MEDIUM,
                 redirect_url: str | None = None,
                 user_photo: bool = False,
                 corner_radius: int | None = None,
                 access_write: bool = True):
        self.telegram_login = telegram_login
        self.corner_radius = corner_radius
        self.size = size
        self.redirect_url = redirect_url
        self.user_photo = user_photo
        self.access_write = access_write
        self.start_script = ('<script async src='
                             '"https://telegram.org/js/telegram-widget.js?22"')
        self.end_script = '></script>'

    def callback_telegram_login_widget(self) -> str:
        """
        Generate Telegram Callback Login Widget.

        If authorization was successful, the method waits for the Javascript
        function 'onTelegramAuth(user)' to be called.
        Example:

        <script type="text/javascript">
            function onTelegramAuth(user) {
            alert(
            'Logged in as ' + user.first_name + ' ' + user.last_name + '!');
            }
            </script>


        :return str:
        """
        data_on_auth = 'data-onauth="onTelegramAuth(user)"'

        params = self._generate_params(self.telegram_login,
                                       self.size,
                                       self.corner_radius,
                                       self.user_photo,
                                       self.access_write)
        return (
            f'{self.start_script} '
            f'{params.get("data_telegram_login")} '
            f'{params.get("data_size")} '
            f'{data_on_auth} '
            f'{params.get("data_user_pic")} '
            f'{params.get("data_radius")} '
            f'{params.get("data_request_access")} '
            f'{self.end_script}'
        )

    def redirect_telegram_login_widget(self):
        redirect_url = f'data-auth-url="{self.redirect_url}"'
        params = self._generate_params(self.telegram_login,
                                       self.size,
                                       self.corner_radius,
                                       self.user_photo,
                                       self.access_write)
        """
        Generate Telegram Callback Login Widget
        :return str:
        """

        return (
            f'{self.start_script} '
            f'{params.get("data_telegram_login")} '
            f'{params.get("data_size")} '
            f'{redirect_url} '
            f'{params.get("data_user_pic")} '
            f'{params.get("data_radius")} '
            f'{params.get("data_request_access")} '
            f'{self.end_script}'
        )

    def _generate_params(self, telegram_login, size, corner_radius, user_photo,
                         access_write):
        data_telegram_login = f'data-telegram-login="{telegram_login}"'
        data_size = f'data-size="{size.value}"'
        data_userpic = f'data-userpic="{user_photo}"' if not user_photo else ''
        data_radius = f'data-radius="{corner_radius}"' if isinstance(
            corner_radius, int) else ''
        data_request_access = f'data-request-access="{access_write}"'
        
        return {
            'data_telegram_login': data_telegram_login,
            'data_size': data_size,
            'data_user_pic': data_userpic,
            'data_radius': data_radius,
            'data_request_access': data_request_access,
        }
