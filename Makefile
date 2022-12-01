# Makefile used by the build workflows
# Makefile targets meant for manual use should go in the repository root

PYTHON_VERSION_REQUIRED ?= 3.9

.EXPORT_ALL_VARIABLES:

poetry_setup: ## Setup virtual env and install dependencies
	deactivate || true
	poetry self update || true
	poetry config virtualenvs.create true
	poetry config virtualenvs.in-project true
	poetry install --with dev --no-interaction -v
.PHONY: poetry_setup

PYTHON_VERSION_INSTALLED=$(shell python3 -c "import sys;t='{v[0]}.{v[1]}'.format(v=list(sys.version_info[:2]));sys.stdout.write(t)")
register_poetry_in_direnv:
ifeq ($(PYTHON_VERSION_REQUIRED), $(PYTHON_VERSION_INSTALLED))
	python3 ../../.update_direnv_envrc_with_venv_and_sourcing_of_dot_env_files.py .envrc --venv .venv
else
	@echo "Local install python version $(PYTHON_VERSION_INSTALLED) does not match required version $(PYTHON_VERSION_REQUIRED)"
endif
.PHONY: register_poetry_in_direnv