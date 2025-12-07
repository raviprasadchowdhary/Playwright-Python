import time

from playwright.sync_api import Playwright

from utils.apiBase import APIUtils


def test_createOrderAndVerify(playwright: Playwright):
    #setup
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("RahulKumar@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Rahul@123")
    page.get_by_role("button", name="Login").click()

    # create order via API and get orderId
    orderId = APIUtils.createOrder(playwright)
    print(f"Order ID from API is: {orderId}")

    # navigate to Orders page and verify placed orderId is present in the Orders list
    page.get_by_role("button", name="ORDERS").click()
    assert orderId == page.locator("tbody tr th").nth(0).text_content()

    page.locator("tr").filter(has_text=orderId).get_by_role("button",name="View").click()

    time.sleep(2)