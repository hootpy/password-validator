test:
	- @pytest --tb=no -v

build:
	- @poetry build -f sdist