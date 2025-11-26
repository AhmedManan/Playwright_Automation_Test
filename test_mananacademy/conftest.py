import pytest, os
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    # Headless=True for CI (GitHub Actions) or check an env variable
    is_ci = os.getenv('CI', 'false') == 'true'
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()
