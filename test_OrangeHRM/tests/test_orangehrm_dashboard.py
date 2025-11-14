import re
import pytest
from playwright.sync_api import Page, expect
from ..pages.login_page import LoginPage
from ..pages.dashboard_page import DashboardPage
from ..tests import test_orangehrm_login

def test_dashboard_sidebar(page: Page):
    test_orangehrm_login.test_login(page)
    dashboard_page = DashboardPage(page)
    dashboard_page.is_sidebar_links_visible()