import re
from playwright.sync_api import expect

def test_landing_page_title(page):
    page.goto("https://mananacademy.com/")

    try:
        page.get_by_role("button", name="accept all").click(timeout=5000)
    except:
        print("no popup")

    expect(page).to_have_title(re.compile("Manan Academy - For Learners", re.IGNORECASE))