import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

class Config:
    """Project configuration."""
    
    # Base URLs
    BASE_API_URL = os.getenv("BASE_API_URL", "https://api.simulated-identity-provider.com")
    BASE_UI_URL = os.getenv("BASE_UI_URL", "https://www.saucedemo.com")
    
    # Timeouts
    TIMEOUT_DEFAULT = int(os.getenv("TIMEOUT_DEFAULT", 10))
    TIMEOUT_SHORT = int(os.getenv("TIMEOUT_SHORT", 5))
    
    # Credentials (Test Data for SauceDemo)
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "standard_user")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "secret_sauce")
    LOCKED_USER = os.getenv("LOCKED_USER", "locked_out_user")
    
    # Reporting
    ALLURE_RESULTS_DIR = "reports/allure-results"
    
    # Browser
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    BROWSER = os.getenv("BROWSER", "chrome")
