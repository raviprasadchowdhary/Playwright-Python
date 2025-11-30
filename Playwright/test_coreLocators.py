import time

from playwright.sync_api import Page, expect, Playwright


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

def test_firefox_browser(playwright: Playwright):
    firefox = playwright.firefox
    browser = firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning1")
    page.get_by_role("combobox").select_option("stud")
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()