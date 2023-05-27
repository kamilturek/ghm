update-requirements:
	pip-compile -o requirements/base.txt pyproject.toml
	pip-compile --extra dev -o requirements/dev.txt pyproject.toml

.PHONY: update-requirements
