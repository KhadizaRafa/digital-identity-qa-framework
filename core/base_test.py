import pytest
import logging
from core.logger import log

class BaseTest:
    """Base test class for all tests."""
    
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """Auto-use fixture for logging test start and end."""
        log.info(f"Starting test: {self.__class__.__name__}")
        yield
        log.info(f"Finished test: {self.__class__.__name__}")
