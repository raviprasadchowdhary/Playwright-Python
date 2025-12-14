import json

import pytest
from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils

with open("Playwright/Framework/Data/credentials.json") as f:
    test_data = json.load(f)
    test_credentials = test_data["credentials"]
print(f"Test data loaded from json file: {test_data}")


@pytest.mark.parametrize("test_credentials_list", test_credentials)
def test_e2eTest_createOrderAndVerify(playwright: Playwright, test_credentials_list):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")

    page.get_by_placeholder("email@example.com").fill(test_credentials_list["username"])
    page.get_by_placeholder("enter your passsword").fill(test_credentials_list["password"])
    page.get_by_role("button", name="Login").click()

    orderId = APIUtils.createOrder(playwright, userCredentials=test_credentials_list)

    OrderButton = page.get_by_role("button", name="Orders")
    expect(OrderButton).to_be_visible()
    OrderButton.click()

    page.locator("tr").filter(has_text=orderId).get_by_role("button", name="View").click()

    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
