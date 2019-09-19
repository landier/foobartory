.DEFAULT_GOAL := all
.PHONY : all init run test clean

all: init run test

init:
	python3 -m venv env
	env/bin/pip install -r requirements.txt

run:
	env/bin/python3 foobartory/foobartory.py

test:
	-env/bin/flake8
	TEST=1 env/bin/pytest

clean:
	rm -rf env
