import os
from typing import Any, Dict

import requests


class Content:
    @staticmethod
    def get_content(session_info: Dict[str, Any]) -> Dict[str, str]:
        """
        Fetch content from the API.

        Args:
            session_info: Session information to send to the API

        Returns:
            Dict containing title and text

        Raises:
            requests.exceptions.RequestException: If API request fails
        """
        api_address = os.getenv("API_ADDRESS")
        if not api_address:
            raise ValueError("API_ADDRESS environment variable is not set")

        try:
            response = requests.post(url=api_address, json=session_info, timeout=10)
            response.raise_for_status()
            content = response.json()
            # Validate response structure
            if not isinstance(content, dict):
                raise ValueError("Invalid response format from API")
            if "title" not in content or "text" not in content:
                raise ValueError("Missing required fields in API response")
        except requests.exceptions.RequestException:
            # Re-raise request exceptions for proper handling
            raise
        except (ValueError, KeyError) as e:
            # Log the error and return default content
            print(f"Error processing API response: {e}")
            content = {"title": "Default Title", "text": "Default Text"}

        return content  # type: ignore[no-any-return]
