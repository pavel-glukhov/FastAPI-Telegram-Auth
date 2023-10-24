# FastAPI-Telegram-Auth
A simple example of implementing authorization on a website using the Telegram login widget.

Telegram Official Documentation: https://core.telegram.org/widgets/login

### Instructions:
 - Set the **TELEGRAM_TOKEN** and **TELEGRAM_LOGIN** environment variables.  
    Examples:
   
 **Linux**
  ```console
      export TELEGRAM_TOKEN=**12345678:aaaaabbbbbcccccdddddeeeeeffffff**
      export TELEGRAM_LOGIN=**MY_TEST_BOT**
  ```
 **Windows (PowerShell)**
  ```powershell
     $Env:TELEGRAM_TOKEN = "12345678:aaaaabbbbbcccccdddddeeeeeffffff"
     $Env:TELEGRAM_LOGIN = "MY_TEST_BOT" 
  ``` 
  
 - Register your domain name using the command **/setdomain** in the @BotFather telegram bot.
 - Create virtual environment and activate it.
 - Install python libraries using the pip command **pip install -r .\requirements.txt**
 - run **python main.py**

### Additional Information:
The project implements the generation of the Telegram Login Widget provided by the **TelegramLoginWidget** class from app.widget.  

#### The class **TelegramLoginWidget()** has two methods:
  - #### Redirect method.
  ```python
  redirect_telegram_login_widget()
  # Returns JavaScript code to redirect to the Telegram Login Widget.
  ```

 - #### Callback method.
 ```python
 callback_telegram_login_widget()
 # Returns JavaScript code for the callback of the Telegram Login Widget.
 ```
If authorization was successful, the method waits for the Javascript function to be called.

### Example:
 ```python
 callback_widget = callback_telegram_login_widget(func='onTelegramAuth', arg='user')
 ```

Put this code in your HTML template:
 ```js
 <script type="text/javascript">
     function onTelegramAuth(user) {
     alert(
     'Logged in as ' + user.first_name + ' ' + user.last_name + '!');
     }
 </script>
 ```

**This code is created only as an example. To use this code, additional mechanisms for issuing tokens and controlling authorized users are required. 
Also, the code structure is not a reference and requires adjustments.**
