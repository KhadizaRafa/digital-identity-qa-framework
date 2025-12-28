# Digital Identity QA Automation Framework

This is a production-ready QA automation framework. It simulates a hybrid approach:
- **API Automation**: Simulates a secure digital identity platform (`requests`, `pytest`).
- **UI Automation**: Tests the **SauceDemo** E-Commerce capability as a demo of UI patterns (`playwright`, `pytest`).

## Why Playwright?

We chose **Playwright** over Selenium for this framework because:
1.  **Reliability**: Playwright's auto-waiting mechanism significantly reduces flaky tests by waiting for elements to be actionable before interacting.
2.  **Speed**: Parallel execution context and faster browser interaction protocols.
3.  **Modern Web**: Native support for Shadow DOM, iFrames, and multiple browser contexts (incognito) in a single test.
4.  **Debugging**: The Trace Viewer provides a full replay of the test execution, making debugging effortless.

## Tech Stack

- **Language**: Python 3.10+
- **API Automation**: `requests`
- **UI Automation**: `playwright` (pytest-playwright)
- **Reporting**: Allure
- **Design Pattern**: Page Object Model (POM)

## Folder Structure

The framework follows a modular architecture:

```
digital-identity-qa-framework/
├── api/                # API Automation
│   ├── tests/          # API test cases (simulated)
│   └── api_client.py   # API interactions wrapper
├── ui/                 # UI Automation (SauceDemo)
│   ├── pages/          # Page Object Models (POM)
│   │   ├── base_page.py
│   │   └── login_page.py
│   └── tests/          # UI test cases
├── core/               # Shared Utilities
│   ├── config.py       # Central configuration
│   └── logger.py       # Logging implementation
├── testdata/           # Data files (JSON)
└── requirements.txt    # Project dependencies
```

## Local Setup

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd digital-identity-qa-framework
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

## How to Run Tests

### Run Tests by Marker

Run all smoke tests (Critical Path):
```bash
pytest -m smoke
```

Run all regression tests:
```bash
pytest -m regression
```

Run only UI tests:
```bash
pytest -m ui
```

### UI Tests (SauceDemo)
Run all UI scenarios with Playwright:
```bash
pytest ui/tests
```

Run with header mode (visible browser):
```bash
pytest ui/tests --headed
```

### API Tests (Simulated)
Run all API scenarios:
```bash
pytest api/tests
```

### Generate Allure Report
```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

## Future Roadmap

- **CI/CD Pipeline**: Integrate GitHub Actions for automatic test execution on Pull Requests.
- **Advanced Reporting**: Auto-publish Allure reports to GitHub Pages or S3.
- **Parallel Execution**: Enable `pytest-xdist` for massive parallelization of UI tests.
- **Containerization**: Dockerize the test execution environment.
