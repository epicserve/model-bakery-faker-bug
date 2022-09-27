MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: test
test: test_py ## Run Python integration tests with coverage

.PHONY: test_py
test_py: ## Run Python tests with coverage
	@pytest -n auto --cov

.PHONY: requirements
requirements: ## Compile new requirement files
	@rm -rf ./requirements*.txt
	@pip-compile --upgrade --generate-hashes --output-file requirements.txt requirements.in
