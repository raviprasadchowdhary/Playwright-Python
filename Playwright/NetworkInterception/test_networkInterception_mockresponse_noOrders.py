import time

from playwright.sync_api import Page


def interceptResponse(route):
    route.fulfill(
        json={"data": [], "message": "No Orders"}
    )


def test_network_interception_no_orders(page: Page):
    # login
    page.goto("https://rahulshettyacademy.com/client")

    page.get_by_placeholder("email@example.com").fill("RahulKumar@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Rahul@123")
    page.get_by_role("button", name="Login").click()

    # intercept the network request to return no orders
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", interceptResponse)

    # click on Orders button
    page.get_by_role("button", name="ORDERS").click()
    message = page.locator(".mt-4").text_content()
    print(f"Message is: {message}")

    assert message.__contains__("You have No Orders to show at this time")

    time.sleep(3)
