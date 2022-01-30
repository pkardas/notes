test-flake8:
	docker-compose build && docker-compose run --rm architecture flake8 .

test-mypy:
	docker-compose build && docker-compose run --rm architecture mypy .

test-pytest:
	docker-compose build && docker-compose run --rm architecture pytest .
