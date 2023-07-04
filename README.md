# FastAPI-Telegram-Auth
Simple example of implementing authorization on a website using the Telegram login widget.

Telegram Official Documentation: https://core.telegram.org/widgets/login


### Instructions for launching the project:
 - First need to create **.env** file and fill in  one according to the **.env.example**.
 - Register your domain name using the command **/setdomain** in the @BotFather telegram bot.
 - Create Virtual Environment and activate one.
 - Install python libs using the command **pip install -r .\requirements.txt**
 - run **Python main.py**

### Additional Information:
The project implements the Telegram Login Widget generation provided by the TelegramLoginWidget class from app.widget.  

#### The class **TelegramLoginWidget()** has to methods:
   - **redirect_telegram_login_widget()**  
        Return JavaScript code with redirect Telegram Login Widget  

 
 - **callback_telegram_login_widget()**  
        Return JavaScript code with the callback Telegram Login Widget.  
\
        If authorization was successful, the method waits for the Javascript
        function to be called.

    Example:

    `callback_widget = callback_telegram_login_widget(func='onTelegramAuth', arg='user')`

    Put this code in your HTML template:  
        `<script type="text/javascript">
            function onTelegramAuth(user) {
            alert(
            'Logged in as ' + user.first_name + ' ' + user.last_name + '!');
            }
        </script>`



**This code is created only as example of the implementation of authorization via Telegram on the website.
For use this code, additional mechanisms for issuing tokens and controlling for authorized users are required. 
Also, the structure of the code is not a reference and requires adjustments.** 