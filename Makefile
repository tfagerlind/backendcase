.PHONY: lint run debug produce clear test

lint:
	docker run --rm -it -v $(CURDIR):/scripts peterdavehello/shellcheck:0.7.1 shellcheck /scripts/producer/produce.sh
	docker run -ti --rm -v $(CURDIR):/apps alpine/flake8:3.5.0 listener/listener.py tester/tests.py
	docker compose run --build --entrypoint sh listener -c "pylint /app/listener.py"
	docker compose run --build --entrypoint sh tester -c "pylint /app/tests.py"

run:
	docker compose up --build

debug:
	docker compose --profile debug up --build

produce:
	./producer/produce.sh

clear:
	curl -X POST localhost:80/clear -H 'Content-Type: application/json' -d '{}'

test:
	docker compose --file compose.test.yml run --build --entrypoint sh tester -c "pytest /app/tests.py"
