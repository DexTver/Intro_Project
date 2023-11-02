# Используйте базовый образ Python
FROM python:3.8

# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Скопируйте файл зависимостей (requirements.txt) в контейнер
COPY requirements.txt .

# Установите зависимости из файла requirements.txt
RUN pip install -r requirements.txt

# Скопируйте все файлы вашего проекта в контейнер
COPY . .

# Определите порт, на котором будет работать ваше приложение внутри контейнера
EXPOSE 8000

# Команда для запуска вашего Django приложения

CMD ["python", "manage.py", "makemigrations", "MyNotes"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
