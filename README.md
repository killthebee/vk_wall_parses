### parser
Парсит посты со стен сообществ в вк, делает облако тэгов.

В корне проекта создать файл `.env.dev` и поместить в него
```
DEBUG=1
SECRET_KEY=<Секретный ключ>
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] 0.0.0.0
vk_login=<Ваш логин вк>
vk_password=<Ваш пароль вк>
```
Для запуска проекта:  
```
docker-compose up -d --build
```
Для запуска тестов:  
```
docker-compose exec web python manage.py test
```
Перейти в `http://127.0.0.1:8000/` 


