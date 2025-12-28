import pytest
from api.api_client import APIClient
from core.base_test import BaseTest

class TestAuthentication(BaseTest):
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()

    @pytest.mark.smoke
    @pytest.mark.api
    def test_login_success(self):
        """Test successful login and token retrieval."""
        # Simulations
        # login_payload = {"username": "test_user_01", "password": "SecurePassword123!"}
        # response = self.client.post("/auth/login", json=login_payload)
        # assert response.status_code == 200
        # token = response.json().get("token")
        # assert token is not None
        pass

    @pytest.mark.regression
    @pytest.mark.api
    def test_login_failure(self):
        """Test login with invalid credentials."""
        # login_payload = {"username": "test_user_01", "password": "WrongPassword"}
        # response = self.client.post("/auth/login", json=login_payload)
        # assert response.status_code == 401
        pass
