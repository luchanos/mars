# MARS project

python manage.py startapp mars_api

# миграции
python manage.py makemigrations
python manage.py migrate

чтобы создать новую БД в консоли пишем:

**createdb mars_db**

удалить БД в консоли пишем:

**dropdb mars_db**

# админка

создание суперпользователя:

**python manage.py createsuperuser**

# todo list
1. Надо понять как работают формы в сочетании со стилями css
2. Прикрутить авторизацию
3. Понять как работают различного рода токены