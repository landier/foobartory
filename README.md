# Foobartory
_Quickstart_
```
git clone https://gitlab.com/landier/foobartory
cd foobartory
make
```

## Requirements
* Python 3 (tested with Python 3.7)
* pip

## Make commands
* __make all__: Execute all following commands
* __make init__: Create virtualenv & install requirements
* __make run__: Execute game
* __make test__: Execute flake8 & unit tests
* __make clean__: Delete virtualenv

## Example
```
...
--------------------
robots: 29
money: 4
foo: 4
bar: 1
foobar: 0
--------------------
robots: 29
money: 4
foo: 5
bar: 1
foobar: 0
--------------------
robots: 29
money: 4
foo: 5
bar: 1
foobar: 0
--------------------
robots: 29
money: 4
foo: 5
bar: 1
foobar: 0
--------------------
robots: 29
money: 4
foo: 6
bar: 1
foobar: 0
--------------------
robots: 30
money: 1
foo: 0
bar: 1
foobar: 0
```

## TODO
* Add multithreading to execute robots in parallel and not sequentially
* Count time execution (in seconds) to completion
