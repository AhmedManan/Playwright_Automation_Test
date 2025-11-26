import re
from playwright.sync_api import Page, expect
from ..pages.landing_page import LandingPage


def test_page_title(page: Page) -> None:
    landing_page = LandingPage(page)

    page.goto("https://MananAcademy.com/")
    expect(page).to_have_title(re.compile('Manan Academy - For Learners', re.IGNORECASE))

def test_page_hero_section(page: Page) -> None:
    landing_page = LandingPage(page)
    page.goto("https://MananAcademy.com/")
    assert landing_page.page_hero_section().is_visible()
