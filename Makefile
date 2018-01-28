REPO=testpypi

all:
	rm -rf dist
	rm -rf build
	python setup.py sdist
	python setup.py bdist_wheel
	twine upload --repository $(REPO) dist/*
