import pytest
from playwright.sync_api import Page, expect
from core.base_test import BaseTest
from core.config import Config
from ui.pages.login_page import LoginPage

class TestSauceDemoLogin(BaseTest):
    
    @pytest.fixture(autouse=True)
    def setup_page(self, page: Page):
        """Fixture to initialize Page Object with Playwright Page."""
        self.login_page = LoginPage(page)
        self.login_page.navigate()
        self.page = page

    @pytest.mark.smoke
    @pytest.mark.ui
    def test_valid_login(self):
        """Verify that a valid user can log in successfully."""
        self.login_page.login(Config.ADMIN_USERNAME, Config.ADMIN_PASSWORD)
        
        # Playwright assertion
        expect(self.page).to_have_url(f"{Config.BASE_UI_URL}/inventory.html")

    @pytest.mark.regression
    @pytest.mark.ui
    def test_locked_out_user(self):
        """Verify that a locked-out user receives the correct error message."""
        self.login_page.login(Config.LOCKED_USER, Config.ADMIN_PASSWORD)
        
        error = self.login_page.get_error_message()
        assert "Epic sadface: Sorry, this user has been locked out." in error

    @pytest.mark.regression
    @pytest.mark.ui
    def test_invalid_credentials(self):
        """Verify that invalid credentials produce an error."""
        self.login_page.login("invalid_user", "invalid_password")
        
        error = self.login_page.get_error_message()
        assert "Epic sadface: Username and password do not match any user in this service" in error
