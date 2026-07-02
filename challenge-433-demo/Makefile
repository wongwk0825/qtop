.DEFAULT_GOAL := help
PYTHON ?= python3
PIP ?= $(PYTHON) -m pip
help: ## Show this help
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'
all: ci-deps test lint build
clean: ## Remove generated output
	rm -rf artifacts build dist .coverage .pytest_cache .ruff_cache *.egg-info
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type f \( -name '*.pyc' -o -name '*.pyo' \) -delete
ci-deps:
	$(PIP) install -r requirements-ci.txt
test:
	$(PYTHON) -m pytest src/ tests/
coverage:
	$(PYTHON) -m coverage run -m pytest src/ tests/
	$(PYTHON) -m coverage report
lint: ruff-check fortifications
ruff-check:
	$(PYTHON) -m ruff check src/ tests/
format-check:
	$(PYTHON) -m ruff format --check src/ tests/
fortifications: ## Check eval() ban and control chars
	@! grep -rn '\beval(' src/ tests/ --include='*.py' 2>/dev/null || (echo "ERROR: eval() found"; exit 1)
	@echo "Fortifications OK"
ci: test lint
build:
	$(PYTHON) -m build --no-isolation
confirm:
	@echo "Are you sure? [y/N]" && read ans && [ $${ans:-N} = y ]
