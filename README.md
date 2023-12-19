Проект Прогнозирования Потребности в Радиаторах
Этот проект представляет собой пример прогнозирования потребности в радиаторах на основе данных с использованием нейронной сети LSTM с помощью FastAPI.

Установка
Клонировать репозиторий: git clone [https://github.com/exem1337/radiator-predict-ai](https://github.com/Air1K/genetic-algorithm.git)
Перейти в папку проекта:
cd radiator-predict-ai

Создать виртуальное окружение:
python -m venv venv

Активировать виртуальное окружение:
На Windows:
venv\Scripts\activate

На macOS и Linux:
source venv/bin/activate

Установить зависимости:
pip install -r requirements.txt

Запуск
После установки всех зависимостей, запустите FastAPI:
uvicorn main:app --reload После этого API будет доступно по адресу http://127.0.0.1:8000. Можете перейти по ссылке в браузере или использовать инструменты для отправки запросов (например, Postman) для взаимодействия с эндпоинтами API.

Использование
/predict: POST запрос для предсказания типа радиатора на основе переданных данных. /load_history: GET запрос для загрузки истории обучения модели. /model_info: GET запрос для получения информации о модели. Пожалуйста, убедитесь, что вы просматриваете документацию к API, чтобы понять, какие данные отправлять и какие ожидать в ответ.

Зависимости
Все зависимости для проекта указаны в файле requirements.txt. Убедитесь, что вы установили их в виртуальное окружение перед запуском проекта. Просто скопируйте этот текст в файл с именем README.md в корневой папке ваш