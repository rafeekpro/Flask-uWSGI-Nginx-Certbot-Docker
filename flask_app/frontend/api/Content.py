import requests
import os


class Content:

    @staticmethod
    def get_content(session_info):
        try:
            response = requests.request(method="POST", url=os.environ['API_ADDRESS'], data=session_info)
            content = response.json()
        except:
            content = { "title": "Default Title", "text": "Default Text" }

        return content