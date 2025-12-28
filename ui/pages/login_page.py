from ui.pages.base_page import BasePage
from core.config import Config

class LoginPage(BasePage):
    """Page Object for the SauceDemo Login Page (Playwright)."""
    
    # Locators (CSS Selectors)
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_CONTAINER = "[data-test='error']"
    
    def navigate(self):
        """Navigates to the login page."""
        self.open_url(Config.BASE_UI_URL)
    
    def login(self, username, password):
        """Performs login action."""
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    def get_error_message(self):
        """Retrieves text from the error alert."""
        return self.get_text(self.ERROR_CONTAINER)
