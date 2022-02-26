PROJECT_DIR := .
APP_DIR := $(PROJECT_DIR)/code

export VIRTUAL_ENV := $(PROJECT_DIR)/.venv
export PYTHONPATH := $(VIRTUAL_ENV)/bin/python3

runserver:
	python manage.py runserver

user:
	python manage.py createsuperuser