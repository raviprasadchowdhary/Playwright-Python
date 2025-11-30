
def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False) # Launch the browser
    context = browser.new_context() # Create a new browser context
    page = context.new_page() # Create a new page in the browser context
    page.goto("https://rahulshettyacademy.com/") # Navigate to the URL