from playwright.sync_api import Page


def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6937107f32ed86587126a601")


def test_networkInterception_unAuthorizedAccess(page: Page):
    # login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("RahulKumar@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Rahul@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", interceptRequest)
    page.get_by_role("button", name="View").nth(0).click()

    message = page.locator(".blink_me").text_content()

    assert message == "You are not authorize to view this order"
