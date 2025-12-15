from playwright.sync_api import Page
from pages.dashboard_page import DashboardPage
from tests import test_orangehrm_login

class TestOrangeHRMDashboard:

    # -------------------------------------------------
    # tests
    # -------------------------------------------------

    def test_dashboard_sidebar(self, page: Page):
        test_orangehrm_login.test_login(page)
        dashboard_page = DashboardPage(page)
        dashboard_page.is_sidebar_links_visible()

    def test_search_field(self, page: Page):
        test_orangehrm_login.test_login(page)
        dashboard_page = DashboardPage(page)
        dashboard_page.searchbar_functionality()

    def test_dashboard_sections_visibility(self, page: Page):
        test_orangehrm_login.test_login(page)
        dashboard_page = DashboardPage(page)
        dashboard_page.is_sections_visible()