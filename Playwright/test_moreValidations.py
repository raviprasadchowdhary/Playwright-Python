from playwright.sync_api import Page, expect


def test_getByPlaceHolder(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # placeholder locator
    # assertion to verify the element is visible
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    # click hide button
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

def test_alerts_dialog(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # handle alert
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()

def test_iframe_handling(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # handle iframe
    frame = page.frame_locator("#courses-iframe")
    # frame.get_by_role("link", name="Learning Paths").click()
    frame.locator("a.text-muted-foreground[href='/learning-paths']").nth(0).click()
    expect(frame.locator("body")).to_contain_text("Learning Journey")