# FastAPI-Telegram-Auth
Simple example of authorization on website using the Telegram Login Widget

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
        The widget require to call JavaScript **onTelegramAuth(user)** function in your HTML Code. See the example below.  
       `<script type="text/javascript">
        function onTelegramAuth(user) {
        alert('Logged in as ' + user.first_name + ' ' + user.last_name + ' (' + user.id + (user.username ? ', @' + user.username : '') + ')');
         }
        </script>`



**This code is created only as example of the implementation of authorization via Telegram on the website.
For use this code, additional mechanisms for issuing tokens and controlling for authorized users are required. 
Also, the structure of the code is not a reference and requires adjustments.** 