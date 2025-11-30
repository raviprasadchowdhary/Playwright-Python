import time

from playwright.sync_api import Page

def test_core_locators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # labels
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    # css selectors
    page.locator("#terms").check()
    time.sleep(3)
    # roles
    page.get_by_role("combobox").select_option("consult")
    # print(page.get_by_role("button"))
    page.get_by_role("button", name="Sign In").click()
    time.sleep(3)