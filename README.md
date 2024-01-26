### Приложение поварской книги на Django

### Установка
Клонируйте репозиторий https://github.com/NadinKon/CulinaryCompanion.git <br>

Установите зависимости с помощью pip: <br>
pip install -r requirements.txt


**Создайте и примените миграции** <br>
python manage.py makemigrations <br>
python manage.py migrate 

**Создайте админа** <br>
python manage.py createsuperuser

### Использование
Запустить локально сервер разработки Django:
python manage.py runserver

Тестировать можно по адресу: <br>
http://127.0.0.1:8000/admin <br>
http://127.0.0.1:8000/show_recipes_without_product <br>
