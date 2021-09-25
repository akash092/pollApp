# pollApp

# For Database model/schema migrations

## If making changes to DB
Change your models (in models.py).
- Run python manage.py makemigrations to create migrations for those changes.
- Run python manage.py migrate to apply those changes to the database.
- pip freeze > requirements.txt to save any new dependency

## If pulling latest DB model changes and applying it to your DB
- Run python manage.py migrate to apply those changes to the database.
- pip install -r requirements.txt to install all the packages
