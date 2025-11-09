import re
from playwright.sync_api import Page, expect


def test_searchbar(page: Page) -> None:
    page.goto("https://mananacademy.com/")
    page.locator("#masthead svg").click()
    page.get_by_role("searchbox", name="Search for:").click()
    page.get_by_role("searchbox", name="Search for:").fill("Software")
    page.get_by_role("searchbox", name="Search for:").press("Enter")
    page.get_by_role("button", name="Search").click()
    expect(page).to_have_url("https://mananacademy.com/?s=software/")
    expect(page).to_have_title("software - Manan Academy")
