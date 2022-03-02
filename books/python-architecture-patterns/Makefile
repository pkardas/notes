test-flake8:
	docker-compose build && docker-compose run --rm api flake8 .

test-mypy:
	docker-compose build && docker-compose run --rm api mypy .

test-pytest:
	docker-compose build && docker-compose run --rm api pytest .
