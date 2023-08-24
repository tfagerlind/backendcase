.PHONY: up down produce lint build

lint:
	docker run --rm -it -v $(CURDIR):/scripts peterdavehello/shellcheck:0.7.1 shellcheck /scripts/producer/produce.sh
	docker run -ti --rm -v $(CURDIR):/apps alpine/flake8:3.5.0 listener/listener.py
	docker compose run --build --entrypoint sh listener -c "pylint /app/listener.py"

run:
	docker compose up --build

clean:
	docker compose down

produce:
	./producer/produce.sh

clear:
	curl -X POST localhost:80/clear -H 'Content-Type: application/json' -d '{}'
