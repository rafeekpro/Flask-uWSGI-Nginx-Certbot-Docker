import pytest
from unittest.mock import patch, MagicMock
import requests
from flask_app.frontend.api.Content import Content


class TestContent:
    """Test suite for Content API class."""

    @patch("flask_app.frontend.api.Content.requests.get")
    def test_get_content_success(self, mock_get):
        """Test successful content retrieval."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "title": "API Title",
            "text": "API Text"
        }
        mock_get.return_value = mock_response
        
        session = {}
        result = Content.get_content(session)
        
        assert result["title"] == "API Title"
        assert result["text"] == "API Text"

    @patch("flask_app.frontend.api.Content.requests.get")
    def test_get_content_api_error(self, mock_get):
        """Test content retrieval with API error."""
        mock_get.side_effect = requests.exceptions.RequestException("API Error")
        
        session = {}
        with pytest.raises(requests.exceptions.RequestException):
            Content.get_content(session)

    @patch("flask_app.frontend.api.Content.requests.get")
    def test_get_content_timeout(self, mock_get):
        """Test content retrieval with timeout."""
        mock_get.side_effect = requests.exceptions.Timeout()
        
        session = {}
        with pytest.raises(requests.exceptions.Timeout):
            Content.get_content(session)