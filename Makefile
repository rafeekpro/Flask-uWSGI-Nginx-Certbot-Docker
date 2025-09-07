.PHONY: help install test lint format clean docker-build docker-up docker-down

help: ## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'

install: ## Install dependencies
	pip install --upgrade pip
	pip install -r flask_app/requirements.txt
	pre-commit install

test: ## Run tests with coverage
	pytest --cov=flask_app --cov-report=term-missing --cov-report=html

lint: ## Run all linters
	black --check flask_app/ tests/
	isort --check-only flask_app/ tests/
	flake8 flask_app/ tests/
	mypy flask_app/ --ignore-missing-imports

format: ## Format code with Black and isort
	black flask_app/ tests/
	isort flask_app/ tests/

security: ## Run security checks
	bandit -r flask_app/ -f json -o bandit-report.json

clean: ## Clean up generated files
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage htmlcov
	rm -rf logs/*.log

docker-build: ## Build Docker images
	docker-compose build

docker-up: ## Start Docker containers
	docker-compose up -d

docker-down: ## Stop Docker containers
	docker-compose down

docker-logs: ## View Docker logs
	docker-compose logs -f

docker-restart: docker-down docker-build docker-up ## Restart Docker containers

ssl-init: ## Initialize SSL certificates
	./init-letsencript.sh

dev: ## Run Flask app in development mode
	cd flask_app && FLASK_ENV=development python app.py

pre-commit: ## Run pre-commit hooks
	pre-commit run --all-files