import pytest
from flask import Flask
from flask_app.app import app as flask_app


@pytest.fixture
def app():
    """Create and configure a test app instance."""
    flask_app.config.update({
        "TESTING": True,
        "DEBUG": False,
        "WTF_CSRF_ENABLED": False,
        "SERVER_NAME": "localhost.localdomain",
    })
    yield flask_app


@pytest.fixture
def client(app):
    """Create a test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Create a test runner for the app's Click commands."""
    return app.test_cli_runner()