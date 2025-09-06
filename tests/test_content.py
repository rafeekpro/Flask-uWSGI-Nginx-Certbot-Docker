from unittest.mock import MagicMock, patch

import pytest
import requests

from flask_app.frontend.api.Content import Content


class TestContent:
    """Test suite for Content API class."""

    @patch("flask_app.frontend.api.Content.requests.post")
    def test_get_content_success(self, mock_post):
        """Test successful content retrieval."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"title": "API Title", "text": "API Text"}
        mock_post.return_value = mock_response

        session = {}
        result = Content.get_content(session)

        assert result["title"] == "API Title"
        assert result["text"] == "API Text"

    @patch("flask_app.frontend.api.Content.requests.post")
    def test_get_content_api_error(self, mock_post):
        """Test content retrieval with API error."""
        mock_post.side_effect = requests.exceptions.RequestException("API Error")

        session = {}
        with pytest.raises(requests.exceptions.RequestException):
            Content.get_content(session)

    @patch("flask_app.frontend.api.Content.requests.post")
    def test_get_content_timeout(self, mock_post):
        """Test content retrieval with timeout."""
        mock_post.side_effect = requests.exceptions.Timeout()

        session = {}
        with pytest.raises(requests.exceptions.Timeout):
            Content.get_content(session)
