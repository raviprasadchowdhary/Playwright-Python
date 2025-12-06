from playwright.sync_api import Playwright

from utils.apiBase import APIUtils


def test_createOrderAndVerify(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("RahulKumar@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Rahul@123")
    page.get_by_role("button", name="Login").click()

    orderId = APIUtils.createOrder(playwright)
    page.get_by_role("button", name="ORDERS").click()
    assert orderId == page.locator("tbody tr th").nth(0).text_content()
