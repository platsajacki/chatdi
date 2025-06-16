run-websockets:
	PYTHONPATH=src uvicorn src.ws_fastapi.main:app --reload --host 0.0.0.0 --port 8001

dev-install:
	pip install -r src/requirements.txt
	pip install -r requirements-dev.txt
	pip install -r src/ws_fastapi/requirements.txt

fmt:
	ruff format src --check || true && ruff format src

lint:
	ruff check src --show-fixes

mypy:
	PYTHONPATH=src DJANGO_SETTINGS_MODULE=chatdi.core.settings mypy src

check:
	make fmt
	make lint
	make mypy

tag:
	make lint
	make test
	git fetch --tags
	git for-each-ref --sort=-creatordate --format '%(refname:short)' refs/tags | head -n 1
	@read -p "Enter tag name: " tag_name; \
	git tag -a "$$tag_name" -m "$$tag_name" && git push origin "$$tag_name"

superuser:
	python src/manage.py createsuperuser

runserver:
	python src/manage.py runserver

static:
	python src/manage.py collectstatic

makemigrations:
	python src/manage.py makemigrations

migrate:
	python src/manage.py migrate

shell:
	python src/manage.py shell

test:
	pytest --cov=src/chatdi src/tests --blockage --cov-report term-missing
