# Используем базовый образ Python
FROM python:3.8

# Устанавливаем переменную окружения для отключения вывода буфера Python
ENV PYTHONUNBUFFERED 1

# Создаем и переходим в рабочую директорию приложения
WORKDIR /app

# Копируем файлы зависимостей в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения в контейнер
COPY . /app/

# Запускаем команду для запуска Django приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]