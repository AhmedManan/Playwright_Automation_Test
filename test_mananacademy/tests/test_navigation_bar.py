import re
from playwright.sync_api import expect

def test_navigation_bar(page):
    page.goto("https://mananacademy.com/")
    page.get_by_role("link", name="Blog").click()
    expect(page).to_have_url("https://mananacademy.com/blog/")
    page.get_by_role("link", name="Videos").click()
    expect(page).to_have_url("https://mananacademy.com/videos/")
    page.get_by_role("link", name="বাংলা (Bengali)").click()
    expect(page).to_have_title(re.compile("হোমপেজ - Manan Academy Bangla", re.IGNORECASE))