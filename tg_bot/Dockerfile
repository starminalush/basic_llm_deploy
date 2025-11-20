FROM python:3.13-slim

# Устанавливаем uv — быстрый менеджер пакетов
RUN pip install uv

# Системные зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /bot

# Копируем pyproject.toml + uv.lock (если есть) из корня проекта
# Если compose использует контекст ".", то путь верный
COPY pyproject.toml uv.lock* ./

# Устанавливаем зависимости
RUN uv sync --no-dev

# Копируем весь код бота
COPY . .

# Запуск
CMD ["uv", "run", "python", "main.py"]
