import requests
from core.config import Config
from core.logger import log

class APIClient:
    """
    Reusable API Client for making HTTP requests.
    Handles base URL, logging, and error raising.
    """

    def __init__(self, base_url=Config.BASE_API_URL):
        self.base_url = base_url
        self.session = requests.Session()
        self.token = None

    def set_token(self, token):
        """Set JWT token for authenticated requests."""
        self.token = token
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def _request(self, method, endpoint, **kwargs):
        """Internal request wrapper with logging."""
        url = f"{self.base_url}{endpoint}"
        log.debug(f"Request: {method} {url} - Data: {kwargs.get('json', kwargs.get('data'))}")

        try:
            response = self.session.request(method, url, timeout=Config.TIMEOUT_DEFAULT, **kwargs)
            log.debug(f"Response: {response.status_code} - {response.text}")
            return response
        except requests.RequestException as e:
            log.error(f"API Request failed: {e}")
            raise

    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)
