from playwright.sync_api import Page, expect


class DashboardPage:
    def __init__(self, page:Page):
        self.page = page
        self.dashboard_heading = page.get_by_role("heading", name="Dashboard")

    def is_dashboard_visible(self):
        expect(self.dashboard_heading).to_be_visible()