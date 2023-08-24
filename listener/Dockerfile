FROM python:3.11.4

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENV PYTHONUNBUFFERED=1

CMD [ "python", "/app/listener.py" ]
