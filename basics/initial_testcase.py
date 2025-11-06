from playwright.sync_api import Playwright, sync_playwright


def run(pw: Playwright) -> None:
    browser = pw.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://youpic.com/")
    page.get_by_role("heading", name="Turn your passion into impact").click()
    page.get_by_role("link", name="Try it now").click()
    page.get_by_role("heading", name="Connect with your favorite").click()

    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="trace.zip")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
