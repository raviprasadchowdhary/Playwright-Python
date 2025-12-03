from playwright.sync_api import Page, expect


def test_UILocators(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # placeholder locator
    # assertion to verify the element is visible
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    # click hide button
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()