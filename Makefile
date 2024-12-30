.PHONY: install test format lint all

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m spacy download en_core_web_sm

test:
	python -m pytest -vv --cov=src \
	--cov=app test/test_*.py
	# --cov specify the root folder for 

format:
	black *.py src/*.py test/*.py

lint:
	pylint --disable=R,C *.py

refactor: format lint

all: install format lint test