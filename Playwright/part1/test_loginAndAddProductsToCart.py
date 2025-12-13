import time

from playwright.sync_api import Page, expect


def test_loginAndAddProductsToCart(page: Page):
    # Add 2 products to the cart after login - iphone X, Nokia Edge
    # Verify that the products are added to the cart successfully
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.locator("#username").fill("rahulshettyacademy")
    page.locator("#password").fill("learning")
    page.locator("#terms").check()
    page.get_by_role("combobox").select_option("consult")
    page.locator("#signInBtn").click()

    appCards = page.locator("app-card")
    iphoneX = appCards.filter(has_text='iPhone X')
    nokiaEdge = appCards.filter(has_text='Nokia Edge')
    iphoneX.get_by_role("button", name="Add").click()
    nokiaEdge.get_by_role("button").click()

    page.get_by_text("Checkout").click()
    expect(page.locator(".media")).to_have_count(2)

    time.sleep(5)
