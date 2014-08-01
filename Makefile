SHELL := /bin/bash

.PHONY: sdist
sdist:
	@python setup.py sdist

.PHONY: bdist_wheel
bdist_wheel:
	@python setup.py bdist_wheel

.PHONY: publish
publish: sdist bdist_wheel
	@twine upload dist/*

.PHONY: clean
clean:
	@rm -rvf MANIFEST *.egg-info *.pyc {,colored_traceback/{,auto/,always/}}{*.pyc,__pycache__}
	@rm -rvf build dist
