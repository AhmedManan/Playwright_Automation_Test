from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def fill_username_password(self, username=str, password=str):
        self.username_input.fill(username)
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()
