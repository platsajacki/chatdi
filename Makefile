dev-install:
	pip install -r src/chatdi/requirements.txt
	pip install -r requirements-dev.txt

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
	python src/chatdi/manage.py createsuperuser

runserver:
	python src/chatdi/manage.py runserver

static:
	python src/chatdi/manage.py collectstatic

makemigrations:
	python src/chatdi/manage.py makemigrations

migrate:
	python src/chatdi/manage.py migrate

shell:
	python src/chatdi/manage.py shell

test:
	pytest --cov=src/chatdi src/chatdi/tests --blockage --cov-report term-missing
