from playwright.sync_api import Page


def test_handleChildWindowsAndTabs(page: Page):
    # Add 2 products to the cart after login - iphone X, Nokia Edge
    # Verify that the products are added to the cart successfully
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPageInfo:
        page.locator(".blinkingText").click()
        childPage = newPageInfo.value

    print(f"\nNewly opened page title is: {childPage.title()}")
    textContent = childPage.locator(".red").text_content()
    print(f"\nRed content is: {textContent}")

    emailId = textContent.split("at")[1].split("with")[0].strip()
    print(f"\nExtracted email id is: {emailId}")
    assert emailId == "mentor@rahulshettyacademy.com"


