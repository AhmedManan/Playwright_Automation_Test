from behave import *
# You can remove 'from playwright.sync_api import Page' as you no longer use it in the signature

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


# ------------------------------------------------------------------
# BDD Test For Login
# ------------------------------------------------------------------

@Given('user is on the login page')
def step_impl(context): # <--- FIX 1
    context.page.goto("https://opensource-demo.orangehrmlive.com/")

@When('user enters valid username & password')
def step_impl(context):
    login_page = LoginPage(context.page)
    login_page.fill_username_password("admin", "admin123")

@When('click on the login button')
def step_impl(context):
    login_page = LoginPage(context.page)
    login_page.click_login()


@Then('the user should be redirected to the dashboard page')
def step_impl(context):
    dashboard_page = DashboardPage(context.page)
    dashboard_page.is_dashboard_visible()