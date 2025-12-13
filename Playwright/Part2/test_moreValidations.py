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

def test_validateTableContent(page:Page):
    # check the price of Rice is 37
    # identify price column
    # identify rice row
    # extract the price value
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for i in range(page.locator("th").count()):
        if page.locator("th").nth(i).filter(has_text="Price").count()>0:
            columnIndex = i
            print(f"Price column index is: {columnIndex}")
            break

    price = page.locator("tr").filter(has_text="Rice").locator("td").nth(columnIndex).text_content()
    print(f"Price of Rice is: {price}")
    assert price == "37"

def test_mouseHover(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # mouse hover to reveal hidden options
    page.get_by_role("button", name="Mouse Hover").hover()
    page.get_by_role("link", name="Top").click()
