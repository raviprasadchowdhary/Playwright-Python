import time

from playwright.sync_api import Page, expect


def test_handleChildWindowsAndTabs(page: Page):
    # Add 2 products to the cart after login - iphone X, Nokia Edge
    # Verify that the products are added to the cart successfully
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPageInfo:
        page.locator(".blinkingText").click()
        childPage = newPageInfo.value

    print(f"\nNewly opened page title is: {childPage.title()}")
    print(f"\nRed content is: {childPage.locator(".red").text_content()}")

