back_and_front endpoints:

Получения списка новостей по методу GET --> https://Nurchik.pythonanywhere.com/news/
Получения деталей новости (detail) по методу GET --> https://Nurchik.pythonanywhere.com/news/detail/2 #id 
новости Создание новости (create) по методу POST --> https://Nurchik.pythonanywhere.com/news/create/ 
Обновление новости (update) по методу POST --> https://Nurchik.pythonanywhere.com/news/update/2 #id новости
Удаление новости (delete) по методу POST --> https://Nurchik.pythonanywhere.com/news/delete/2 #id
Админ панель (Админ) по методу GET --> https://Nurchik.pythonanywhere.com/admin/
новости Пример json строки для создания задания { "id": 1, "title": "1", "description": "1", "date": "2022-10-14T12:59:09.186457Z", "published": false } 
И так далее по всем вашим endpoints
