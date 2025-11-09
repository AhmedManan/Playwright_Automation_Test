import re
from playwright.sync_api import Page, expect


def test_landing_page(page: Page) -> None:
    page.goto("https://mananacademy.com/")
    expect(page).to_have_title("Manan Academy - For Learners")
    expect(page.get_by_text("Topics List Software Quality")).to_be_visible()

    print("Test passed")
