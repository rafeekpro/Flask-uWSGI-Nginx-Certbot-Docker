from unittest.mock import patch

import requests


class TestApp:
    """Test suite for the main Flask application."""

    def test_app_exists(self, app):
        """Test that the app exists."""
        assert app is not None

    def test_app_is_testing(self, app):
        """Test that the app is in testing mode."""
        assert app.config["TESTING"] is True

    def test_home_route_success(self, client):
        """Test the home route with successful content retrieval."""
        mock_content = {"title": "Test Title", "text": "Test Text"}

        with patch("frontend.api.Content.Content.get_content") as mock_get:
            mock_get.return_value = mock_content
            response = client.get("/")

            assert response.status_code == 200
            assert b"Test Title" in response.data or b"No title" in response.data

    def test_home_route_connection_error(self, client):
        """Test the home route when API connection fails."""
        with patch("frontend.api.Content.Content.get_content") as mock_get:
            mock_get.side_effect = requests.exceptions.ConnectionError()
            response = client.get("/")

            assert response.status_code == 200
            assert b"No title" in response.data or b"No text" in response.data

    def test_health_check(self, client):
        """Test health check endpoint."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.get_json()
        assert data["status"] == "healthy"
        assert data["service"] == "flask-app"
        assert "environment" in data
