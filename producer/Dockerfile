FROM debian:12.1

RUN apt-get update && apt-get install -y curl

COPY . /app

CMD [ "sh", "/app/produce.sh" ]
