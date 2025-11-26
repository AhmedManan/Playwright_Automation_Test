from playwright.sync_api import Page, expect


class BlogListPage:

    def __init__(self, page:Page):
        self.page = page