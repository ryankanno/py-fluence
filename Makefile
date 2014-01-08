NOSETESTS ?= nosetests

.PHONY: nosetests nosetests.coverage test test.coverage flake8

test: nosetests flake8
test.coverage: nosetests.coverage flake8

nosetests:
	@$(NOSETESTS) --with-doctest

nosetests.coverage:
	@$(NOSETESTS) --with-xcoverage --cover-package=py_fluence --cover-tests --with-doctest

flake8:
	@flake8 py_fluence tests

clean:
	@rm -rf .coverage
	@rm -rf coverage.xml
