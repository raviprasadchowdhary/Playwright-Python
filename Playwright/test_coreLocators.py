import time

from playwright.sync_api import Page

def test_core_locators_getByLabelAndRole(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # labels
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("123")
    page.get_by_role("combobox").select_option("consult")
    time.sleep(2)