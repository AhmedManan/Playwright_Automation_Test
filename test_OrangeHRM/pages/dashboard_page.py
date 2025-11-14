from playwright.sync_api import Page, expect


class DashboardPage:
    def __init__(self, page:Page):
        self.page = page
        self.dashboard_heading = page.get_by_role("heading", name="Dashboard")
        # self.sidebar_links = page.get_by_role("link", name=['Admin','PIM','Time','Recruitment','My Info','Performance','Dashboard','Directory','Maintenance','Claim','Buzz'])
        self.sidebar_links = [
            page.get_by_role("link", name=name)
            for name in ("Admin", "PIM", "Time", "Recruitment",
                         "My Info", "Performance", "Dashboard",
                         "Directory", "Maintenance", "Claim", "Buzz")
        ]

    def is_dashboard_visible(self):
        expect(self.dashboard_heading).to_be_visible()

    def is_sidebar_links_visible(self):
        for link in self.sidebar_links:
            expect(link).to_be_visible()