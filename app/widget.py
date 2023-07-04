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
     
    :param size: enum [Size.LARGE | Size.MEDIUM | Size.SMALL]
    :param user_photo: bool
    :param corner_radius: integer
    :param access_write: bool
    """
    
    def __init__(self, telegram_login: str,
                 size: Size = Size.MEDIUM,
                 user_photo: bool = False,
                 corner_radius: int | None = None,
                 access_write: bool = True):
        self.telegram_login = telegram_login
        self.corner_radius = corner_radius
        self.size = size
        self.user_photo = user_photo
        self.access_write = access_write
        self.start_script = ('<script async src='
                             '"https://telegram.org/js/telegram-widget.js?22"')
        self.end_script = '></script>'
    
    def callback_telegram_login_widget(self, func: str, arg: str = '') -> str:
        """
        Generate Telegram Callback Login Widget.
        
        :param str func: - JS function that have to call
        :param str arg: - argument for JS function
        
        If authorization was successful, the method waits for the Javascript
        function to be called.
        Example:
        callback_telegram_login_widget
        widget = callback_telegram_login_widget(func='onTelegramAuth',
                                                arg='user')
        
        Put this code to your HTML template:
            <script type="text/javascript">
            function onTelegramAuth(user) {
            alert(
            'Logged in as ' + user.first_name + ' ' + user.last_name + '!');
            }
            </script>
        
        :return str: Return JS code with widget
        """
        data_on_auth = f'data-onauth="{func}({arg})"'
        
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
    
    def redirect_telegram_login_widget(self, redirect_url: str):
        """
        Generate Telegram Callback Login Widget
        :param str redirect_url: - The URL to which the redirection
                                      should take for authorization.

        :return str: Return JS code with widget
        """
        
        params = self._generate_params(self.telegram_login,
                                       self.size,
                                       self.corner_radius,
                                       self.user_photo,
                                       self.access_write)
        return (
            f'{self.start_script} '
            f'{params.get("data_telegram_login")} '
            f'{params.get("data_size")} '
            f'data-auth-url="{redirect_url}" '
            f'{params.get("data_user_pic")} '
            f'{params.get("data_radius")} '
            f'{params.get("data_request_access")} '
            f'{self.end_script}'
        )
    
    def _generate_params(self, telegram_login: str, size: Size,
                         corner_radius: int | None = None,
                         user_photo: bool = False,
                         access_write: bool = True):
        """
        :param str telegram_login:
        :param Size size:
        :param int| None corner_radius:
        :param bool user_photo:
        :param bool access_write:
        :return: str
        """
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
