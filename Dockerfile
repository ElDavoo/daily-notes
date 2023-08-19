FROM python:3-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app.py app.py

CMD ["python", "/app/app.py"]