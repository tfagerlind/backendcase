.PHONY: up down produce lint build

lint:
	docker run -ti --rm -v $(CURDIR):/apps alpine/flake8:3.5.0 listener/listener.py
	docker run --rm -v $(CURDIR):/data cytopia/pylint listener/listener.py

run:
	docker compose up --build

clean:
	docker compose down

produce:
	./producer/produce.sh
