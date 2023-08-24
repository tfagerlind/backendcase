FROM python:3.11.4

RUN pip install \
        pylint==2.17.5 \
        pytest==7.4.0 \
        requests==2.31.0

COPY . /app

WORKDIR /app

CMD [ "pytest", "/app/tests.py" ]
