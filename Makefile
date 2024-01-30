run: test test-cov
test:
	pytest .
test-cov:
	pytest -v --cov=. --cov-report=html