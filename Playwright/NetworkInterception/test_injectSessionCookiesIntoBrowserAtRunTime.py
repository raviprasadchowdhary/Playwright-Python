
def test_injectSessionCookiesIntoBrowserAtRunTime(playwright: Playwright):
    browser = playwright.chromium.laumch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahuleshettyacademy.com/")