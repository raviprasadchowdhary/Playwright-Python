
def test_playwrightBasicsGoToPage(playwright):
    browser = playwright.chromium.launch(headless=False) # Launch the browser
    context = browser.new_context() # Create a new browser context
    page = context.new_page() # Create a new page in the browser context
    page.goto("https://rahulshettyacademy.com/") # Navigate to the URL

def test_playwrightBasicsGoToPageShortcut(page):
    page.goto("https://rahulshettyacademy.com/") # Navigate to the URL
    # The browser and context are managed automatically by the fixture
    # Here default is headless=True
    # Here chromium browser is used by default
    # No need to manually launch or close the browser
    # The page fixture provides a new page for each test function
    # The browser will be closed automatically after the test function completes
    # This is a more concise way to write the test using the built-in page fixture
    # No need to create browser or context objects explicitly
    # The page fixture handles all of that behind the scenes
    # This makes the test code cleaner and easier to read
    # The page fixture is provided by the Playwright pytest plugin
    # It is a convenient way to work with Playwright in pytest
    # The page fixture is scoped to the test function by default
    # This means a new page is created for each test function
    # This ensures test isolation and prevents state leakage between tests
    # Overall, using the page fixture is the recommended way to write Playwright tests in pytest
