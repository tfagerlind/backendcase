FROM python:3.11.4

RUN pip install \
        flask==2.3.3 \
        jsonschema==4.19.0 \
        pymongo==4.5.0 \
        pylint==2.17.5

COPY . /app

WORKDIR /app

ENV PYTHONUNBUFFERED=1

CMD [ "flask", "--app", "listener", "run", "--host", "0.0.0.0", "--port", "80" ]
