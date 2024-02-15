.PHONY: lint test

lint:
	docker-compose run web flake8 main.py

test:
	docker-compose run web python3 test_main.py

