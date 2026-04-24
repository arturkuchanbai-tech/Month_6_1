FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# сначала зависимости (для кеша)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# потом весь проект
COPY . .