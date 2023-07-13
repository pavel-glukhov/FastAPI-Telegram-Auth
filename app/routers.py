import os

from fastapi import APIRouter, Depends, Request, status
from starlette.responses import HTMLResponse, RedirectResponse

from app.config import load_config
from app.auth.exceptions import TelegramDataError, TelegramDataIsOutdated
from app.auth.schemes import TelegramAuth
from app.auth.validators import validate_telegram_data
from app.auth.widget import Size, TelegramLoginWidget
from starlette.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory=os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "templates"))


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
    redirect_url = str(request.url_for('login'))
    
    widget = TelegramLoginWidget(telegram_login=telegram_login,
                                 size=Size.LARGE,
                                 user_photo=False,
                                 corner_radius=0)
    redirect_widget = widget.redirect_telegram_login_widget(
        redirect_url=redirect_url)
    
    context = {
        'request': request,
        'telegram_login_widget': redirect_widget
    }
    
    if not params.dict().get('hash'):
        return templates.TemplateResponse('login.html', context=context)
    
    try:
        result = validate_telegram_data(telegram_token, params)
    
    except TelegramDataIsOutdated:
        return HTMLResponse('The authentication data is expired.',
                            status_code=status.HTTP_401_UNAUTHORIZED)
    except TelegramDataError:
        return HTMLResponse('The request contains invalid data.',
                            status_code=status.HTTP_400_BAD_REQUEST)
    
    if result:
        return templates.TemplateResponse('profile.html',
                                          context={'request': request,
                                                   **result})
