from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils


def test_injectSessionCookiesIntoBrowserAtRunTime(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # here we are getting the token by calling the API directly and then injecting that token into the browser's local storage
    # before navigating to the page. This way, we bypass the login process.
    # this is useful when we want to test pages that require authentication without going through the login UI.
    api_utils = APIUtils()
    token = api_utils.getToken(playwright)
    print(f"Token is: {token}")
    page.add_init_script(f"""localStorage.setItem("token", "{token}")""")

    page.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")
    page.get_by_role("button", name="ORDERS").first.click()
    expect(page.get_by_text("Your Orders")).to_be_visible()