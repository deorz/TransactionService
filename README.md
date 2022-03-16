# TransactionService
#### Description:
TransactionService is a service where you can create account and provide transactions using your wallets.



#### Stack:

- Python 3.8
- Django Framework 2.2.16
- psycopg2

#### Database:
- PostgreSQL with psycopg connector



#### Installation:

1. Install and activate virtual environment(venv)

   ```python
   python -m venv venv
   ```
   
2. Create PostgreSQL database and configure connection in transaction_service/settings.py
   ```python
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{DATABASE_NAME}',
        'USER': '{DATABASE_USER}',
        'PASSWORD': '{DATABASE_USER_PASSWD}',
        'HOST': '{127.0.0.1 or localhost}',
        'PORT': '{5432 or which one you choose}',
        }
    }
    ```

4. Install all dependencies from requirements.txt

   ```python
   pip install -r requirements.txt
   ```

5. Run server in manage.py directory:

   ```python
   python manage.py runserver
   ```

   

4. Enjoy!

------

​																																									Author: deorz
