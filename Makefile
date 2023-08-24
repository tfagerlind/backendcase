.PHONY: up down produce

run:
	docker compose up --build

clean:
	docker compose down

produce:
	./producer/produce.sh
