FROM python:3.9-slim

WORKDIR /app

RUN apt-get update
RUN apt-get -y install libpq-dev gcc

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]
