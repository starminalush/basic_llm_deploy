FROM python:3.13-slim

# Устанавливаем uv (официальный способ)
RUN pip install uv

# Системные зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем pyproject.toml (uv будет устанавливать зависимости из него)
COPY pyproject.toml uv.lock* ./

# Устанавливаем зависимости из pyproject через uv
RUN uv sync --no-dev


# Копируем все файлы проекта
COPY . .

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app","--host", "0.0.0.0", "--port", "8000"]
