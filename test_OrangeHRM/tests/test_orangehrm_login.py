import re
from playwright.sync_api import Page, expect
from ..pages.login_page import LoginPage
from ..pages.dashboard_page import DashboardPage


def test_login(page: Page) -> None:
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/")
    login_page.login('Admin', 'admin123')
    dashboard_page.is_dashboard_visible()

