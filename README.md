## Проект API автотестов для reqres.in


<!-- Технологии -->

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/pytest.png"></code>
  <code><img width="5%" title="Requests" src="images/requests.png"></code>
  <code><img width="5%" title="Jenkins" src="images/jenkins.png"></code>
  <code><img width="5%" title="Allure Report" src="images/allure_report.png"></code>
  <code><img width="5%" title="Telegram" src="images/tg.png"></code>
</p>

<!-- Тест кейсы -->

### Что проверяем

* Создание пользователя: валидация формата ответа
* Удаление пользователя
* Получение данных одного пользователя
* Получение ресурса: валидация формата ответа
* Просмотр несуществущего пользователя
* Просмотр списка пользователей на конкретной странице
* Получение списка пользователей: валидация формата ответа 
* Успешная регистрация пользователя
* Регистрация пользователя с пустыми данными
* Изменение данных пользователя

## Запуск тестов
### Для локального запуска
1. Склонируйте репозиторий
2. Откройте проект в PyCharm
3. Введите в терминале команду
``` 
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install --no-root
pytest .
```

<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="images/jenkins.png"> Запуск проекта в Jenkins
### [Job](https://jenkins.autotests.cloud/job/selenamond_reqres_api/)
##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение
![This is an image](images/screenshots/jenkins_start.png)
##### При нажатии на иконку Allure Report откроется отчет о прохождении тестов
![This is an image](images/screenshots/allure_jenkins.png)


<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/allure_report.png"> Allure report
##### После прохождения тестов, результаты можно посмотреть в Allure отчете, где так же содержится ссылка на Jenkins
![This is an image](images/screenshots/allure_overview.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](images/screenshots/allure_graphs.png)

##### Во вкладке Suites находятся собранные тест кейсы со статусом выполнения, описанием теста, curl запроса и ответ в формате json
![This is an image](images/screenshots/allure_suites.png)

#### Если тест запускался локально:
Необходимо ввести в терминале команду: 
```
allure serve allure-results
``` 


<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/tg.png"> Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и информацией о выполненных тестах
![This is an image](images/screenshots/tg_allure.png)
