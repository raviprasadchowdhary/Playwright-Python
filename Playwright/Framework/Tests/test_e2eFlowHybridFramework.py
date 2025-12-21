import json

import pytest
from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import page

from Playwright.Framework.PageObjects.common import Common
from Playwright.Framework.PageObjects.loginPage import LoginPage
from utils.apiBaseFramework import APIUtils

with open("Playwright/Framework/Data/credentials.json") as f:
    test_data = json.load(f)
    test_credentials = test_data["credentials"]
print(f"Test data loaded from json file: {test_data}")

@pytest.mark.smoke
@pytest.mark.e2e
@pytest.mark.parametrize("test_credentials_list", test_credentials)
def test_e2eTest_createOrderAndVerify(playwright: Playwright, browser_instance, test_credentials_list):
    # here we will create order by API call
    orderId = APIUtils.createOrder(playwright, userCredentials=test_credentials_list)

    # here we will log in to the application and verify orderId in UI
    loginPage = LoginPage(browser_instance)
    loginPage.navigate()
    dashboardPage = loginPage.login(test_credentials_list)
    orderDetailsPage = dashboardPage.click_order_button()
    orderDetailsPage.clickViewByOrderId(orderId)

    # here we will add assertion to verify orderId in UI
    expect(browser_instance.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
