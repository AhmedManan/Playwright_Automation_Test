import re
import pytest
from playwright.sync_api import Page, expect
from ..pages.login_page import LoginPage
from ..pages.dashboard_page import DashboardPage

def get_csv_data() -> list:
    import csv
    data = []
    with open("./test_OrangeHRM/test_data/login_data.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

@pytest.mark.parametrize("username, password", get_csv_data())
def test_login(page: Page, username, password) -> None:
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/")
    login_page.login(username, password)
    dashboard_page.is_dashboard_visible()

@pytest.mark.parametrize("username, password", get_csv_data())
def test_invalid_login(page: Page, username, password) -> None:
    login_page = LoginPage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/")
    login_page.login(username, password)
    expect(page).get_by_text("Invalid credentials").is_visible()
