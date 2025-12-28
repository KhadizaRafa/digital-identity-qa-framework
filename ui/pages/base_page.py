from playwright.sync_api import Page, Locator
from core.logger import log

class BasePage:
    """Base Page for Playwright POM strategy."""
    
    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url: str):
        """Navigate to a URL."""
        self.page.goto(url)
        log.info(f"Opened URL: {url}")

    def click(self, selector: str):
        """Click element."""
        self.page.click(selector)
        log.info(f"Clicked element: {selector}")

    def fill(self, selector: str, text: str):
        """Fill text into element."""
        self.page.fill(selector, text)
        log.info(f"Filled '{text}' into: {selector}")

    def get_text(self, selector: str) -> str:
        """Get text from element."""
        return self.page.text_content(selector)

    def get_current_url(self) -> str:
        return self.page.url
