fmt:
	poetry run black .
	poetry run isort .

lint: 
	poetry run pflake8 .
	poetry run mypy .

pytest:
	poetry run pytest .
