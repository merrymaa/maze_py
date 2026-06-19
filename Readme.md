# A1_Maze_Python

После клонирования репозитория необходимо:
1. Создать виртуальное окружение:
``python -m venv venv``

2. Активировать виртуальное окружение

  * Windows: ``venv\Scripts\activate``

  * macOS/Linux: ``source venv/bin/activate``

3. Установить зависимости: ``pip install -r requirements.txt``


## Запуск десктопного приложения (из src):
``py -m desktop.maze_app
``

или

``make run-desktop``

## Запуск веб версии (из src):
``uvicorn web.maze_web:app --reload``

или

``make run-web``