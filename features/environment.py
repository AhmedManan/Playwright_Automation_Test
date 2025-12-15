from playwright.sync_api import sync_playwright


def before_all(context):
    """Initializes the Playwright object."""
    # Launch the Playwright service once
    context.playwright = sync_playwright().start()


def before_scenario(context, scenario):
    """
    HOOK that runs before every scenario.
    This creates and attaches context.page, fixing the AttributeError.
    """
    # Launch a browser
    context.browser = context.playwright.chromium.launch(headless=False)

    # CREATE AND ATTACH THE 'page' OBJECT TO THE CONTEXT
    context.page = context.browser.new_page()


def after_scenario(context, scenario):
    """Closes the browser after each scenario runs."""
    if hasattr(context, 'browser'):
        context.browser.close()


def after_all(context):
    """Stops the Playwright environment."""
    if hasattr(context, 'playwright'):
        context.playwright.stop()