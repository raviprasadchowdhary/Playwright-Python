import time

from playwright.sync_api import Page, expect


def test_core_locators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # labels
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning1")
    # css selectors
    page.locator("#terms").check()
    # roles
    page.get_by_role("combobox").select_option("consult")
    # print(page.get_by_role("button"))
    page.get_by_role("button", name="Sign In").click()
    # Auto-wait
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()