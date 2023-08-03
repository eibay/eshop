FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt
    # adduser \
    # --disabled-password \
    # --no-create-home \
    # django-user

COPY . .

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "localhost:8000"]
# USER django-user