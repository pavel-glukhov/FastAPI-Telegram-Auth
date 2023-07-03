from fastapi import APIRouter, Depends, Request
from starlette.responses import HTMLResponse, RedirectResponse

from app.config import load_config, templates
from app.exceptions import TelegramDataError, TelegramDataIsOutdated
from app.schemes import TelegramAuth
from app.validators import verify_telegram_authentication
from app.widget import Size, TelegramLoginWidget

router = APIRouter()


@router.get("/", name='index')
async def index(request: Request):
    """
    Index page just redirects to login page.
    """
    return RedirectResponse(url=request.url_for('login'))


@router.get("/login", name='login')
async def login(request: Request,
                params: TelegramAuth = Depends(TelegramAuth)):
    """
    Endpoint for authorization through Telegram API.

    If there is no "hash" in query, it is automatically
    redirected to the authorization 'login' page.

    If a "hash" is received in query parameters,
    a function is called to validate the received data and, if successful,
    renders a page with information about the authorized user.
    """

    config = load_config()
    telegram_token = config.bot.telegram_token
    telegram_login = config.bot.telegram_login
    auth_url = str(request.url_for('login'))

    widget = TelegramLoginWidget(telegram_login=telegram_login,
                                 size=Size.LARGE,
                                 redirect_url=auth_url,
                                 user_photo=False,
                                 corner_radius=0)
    telegram_login_widget = widget.redirect_telegram_login_widget()
    context = {
        'request': request,
        'telegram_login_widget': telegram_login_widget
    }

    if not params.dict().get('hash'):
        return templates.TemplateResponse('login.html', context=context)

    try:
        result = verify_telegram_authentication(telegram_token, params.dict())

    except TelegramDataIsOutdated:
        return HTMLResponse('The authentication data is expired..')
    except TelegramDataError:
        return HTMLResponse('The request contains invalid data')

    if result:
        return templates.TemplateResponse('profile.html',
                                          context={'request': request,
                                                   **result}
                                          )