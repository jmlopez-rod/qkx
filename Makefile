# qkx makefile

all: install-user

install:
	python setup.py install

install-user:
	python setup.py install --user

build:
	python setup.py sdist

develop:
	python setup.py develop --user

clean:
	rm -rf qkx.egg-info
	rm -rf build

pypi:
	python setup.py sdist upload
