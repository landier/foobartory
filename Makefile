.DEFAULT_GOAL := all
.PHONY : all install lint test build upload clean

all: init test clean

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
