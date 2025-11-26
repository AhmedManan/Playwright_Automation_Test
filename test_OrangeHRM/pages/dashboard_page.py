from playwright.sync_api import Page, expect


class DashboardPage:

    def __init__(self, page:Page):
        self.page = page

        # -------------------------------------------------
        # page locators
        # -------------------------------------------------

        self.dashboard_heading = page.get_by_role("heading", name="Dashboard")
        self.sidebar_link_names = ("Admin", "PIM", "Time", "Recruitment",
                                   "My Info", "Performance", "Dashboard",
                                   "Directory", "Maintenance", "Claim", "Buzz")

        self.sidebar_links = [
            page.get_by_role("link", name=name)
            for name in self.sidebar_link_names
        ]
        self.section_time_at_work = page.get_by_text("Time at Work")
        self.section_my_actions = page.get_by_text("My Actions")
        self.section_quick_launch = page.get_by_text("Quick Launch")
        self.section_buzz_Latest_posts =page.get_by_text("Buzz Latest Posts")
        self.section_employees_on_leave_today=page.get_by_text("Employees on Leave Today")
        self.section_employee_distribution_by_sub = page.get_by_text("Employee Distribution by Sub")
        self.section_employee_distribution_by_location = page.get_by_text("Employee Distribution by Location")


        self.search_field = page.get_by_role("textbox", name="Search")

    # -------------------------------------------------
    # page actions
    # -------------------------------------------------

    def is_dashboard_visible(self):
        expect(self.dashboard_heading).to_be_visible()

    def is_sidebar_links_visible(self):
        for link in self.sidebar_links:
            expect(link).to_be_visible()

    def is_sections_visible(self):
        expect(self.section_time_at_work).to_be_visible()
        expect(self.section_my_actions).to_be_visible()
        expect(self.section_quick_launch).to_be_visible()
        expect(self.section_buzz_Latest_posts).to_be_visible()
        expect(self.section_employees_on_leave_today).to_be_visible()
        expect(self.section_employee_distribution_by_sub).to_be_visible()
        expect(self.section_employee_distribution_by_location).to_be_visible()

    def searchbar_functionality(self):
        self.search_field.click()

        for name in self.sidebar_link_names:
            link = self.page.get_by_role("link", name=name)
            self.search_field.fill(name)
            self.page.wait_for_timeout(700)
            expect(link).to_be_visible()
            self.search_field.clear()