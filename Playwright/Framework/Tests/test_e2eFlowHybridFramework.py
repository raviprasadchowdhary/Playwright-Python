import json

import pytest
from playwright.sync_api import Playwright, expect

from Playwright.Framework.PageObjects.dashboardPage import DashboardPage
from Playwright.Framework.PageObjects.loginPage import LoginPage
from Playwright.Framework.PageObjects.ordersPage import OrdersPage
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

    loginPage = LoginPage(page)
    loginPage.navigate()

    loginPage.login(test_credentials_list)

    orderId = APIUtils.createOrder(playwright, userCredentials=test_credentials_list)

    dashboardPage = DashboardPage(page)
    dashboardPage.click_order_button()

    # page.locator("tr").filter(has_text=orderId).get_by_role("button", name="View").click()
    orderDetailsPage = OrdersPage(page)
    orderDetailsPage.clickViewByOrderId(orderId)

    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
