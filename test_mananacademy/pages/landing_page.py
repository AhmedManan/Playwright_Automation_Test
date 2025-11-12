from playwright.sync_api import Page


class LandingPage:

    def __init__(self, page: Page):
        self.page = page
        self.page_title = page.get_by_role("div", name="Title")

    def get_page_title(self):
        return self.page_title.inner_text()

    def page_hero_section(self):
        return self.page.get_by_role("heading", name="An Easy Learning Platform for")