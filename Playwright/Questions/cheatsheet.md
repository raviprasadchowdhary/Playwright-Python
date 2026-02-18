# 📘 Playwright + Python + Pytest — Cheatsheet

> A quick-reference guide covering Python, Pytest, and Playwright concepts with real examples from this codebase.  
> Use this for studying, revising, and preparing for interviews or assessments.

---

## Table of Contents

- [1. Python Essentials](#1-python-essentials)
- [2. Pytest Essentials](#2-pytest-essentials)
- [3. Playwright — Browser & Page Setup](#3-playwright--browser--page-setup)
- [4. Playwright — Locators](#4-playwright--locators)
- [5. Playwright — Assertions (expect)](#5-playwright--assertions-expect)
- [6. Playwright — Actions](#6-playwright--actions)
- [7. Playwright — Waits & Auto-Wait](#7-playwright--waits--auto-wait)
- [8. Playwright — Network Interception](#8-playwright--network-interception)
- [9. Playwright — API Testing](#9-playwright--api-testing)
- [10. Playwright — iFrames, Dialogs, Child Windows](#10-playwright--iframes-dialogs-child-windows)
- [11. Playwright — Tracing & Debugging](#11-playwright--tracing--debugging)
- [12. Playwright — Session / Cookie Injection](#12-playwright--session--cookie-injection)
- [13. Page Object Model (POM)](#13-page-object-model-pom)
- [14. Data-Driven Testing](#14-data-driven-testing)
- [15. conftest.py — Fixtures & Hooks](#15-conftestpy--fixtures--hooks)
- [16. Pytest CLI Commands — Quick Reference](#16-pytest-cli-commands--quick-reference)

---

## 1. Python Essentials

### Data Types

```python
# Numeric
x = 10          # int
y = 3.14        # float
z = 2 + 3j      # complex

# Sequence
my_list  = [1, 2, 3]       # mutable
my_tuple = (1, 2, 3)       # immutable
my_range = range(5)         # 0,1,2,3,4

# Text, Mapping, Set, Boolean
my_str  = "hello"
my_dict = {"key": "value"}
my_set  = {1, 2, 3}
flag    = True
```

### List vs Tuple

| Feature | List `[]` | Tuple `()` |
|---------|-----------|------------|
| Mutable | ✅ Yes | ❌ No |
| Performance | Slower | Faster |
| Use Case | Dynamic data | Fixed / config data |

### List of Dictionaries (common for test data)

```python
users = [
    {"username": "user1@mail.com", "password": "pass1"},
    {"username": "user2@mail.com", "password": "pass2"},
]
for user in users:
    print(user["username"])
```

### Lambda, Map, Filter

```python
# Lambda — anonymous inline function
square = lambda x: x ** 2

# Map — apply function to every element
doubled = list(map(lambda x: x * 2, [1, 2, 3]))       # [2, 4, 6]

# Filter — keep elements matching condition
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3])) # [2]
```

### Sorting

```python
nums = [5, 1, 3]
nums.sort()                          # in-place → [1, 3, 5]
sorted_nums = sorted(nums, reverse=True)  # new list → [5, 3, 1]

# Sort list of dicts
users.sort(key=lambda u: u["username"])
```

### OOP — Classes, Inheritance, super()

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)   # call parent constructor
        self.age = age
```

### Instance vs Class vs Static Methods

| Type | Decorator | First Param | Accesses |
|------|-----------|-------------|----------|
| Instance | none | `self` | Instance + class data |
| Class | `@classmethod` | `cls` | Class data only |
| Static | `@staticmethod` | none | Nothing — utility |

### File I/O

```python
with open("file.txt", "r") as f:
    content = f.read()

with open("file.txt", "w") as f:
    f.write("hello")
```

### Exception Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("No error")        # runs only if no exception
finally:
    print("Always runs")     # cleanup — runs no matter what
```

### Sync vs Async

```python
# Default: synchronous (blocking)
import time
time.sleep(2)                # blocks

# Async with asyncio
import asyncio

async def fetch():
    await asyncio.sleep(2)   # non-blocking

asyncio.run(fetch())
```

---

## 2. Pytest Essentials

### Test Discovery Rules

- Files must match `test_*.py` or `*_test.py`
- Functions must start with `test_`
- Classes must start with `Test`

### Fixtures

```python
import pytest

@pytest.fixture(scope="function")   # scope: function | class | module | session
def browser_instance(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    yield page                      # ← provide to test
    context.close()                 # ← teardown (runs after test)
    browser.close()
```

### Fixture Scopes

| Scope | Created / Destroyed |
|-------|---------------------|
| `function` | Once per test function (default) |
| `class` | Once per test class |
| `module` | Once per test file |
| `session` | Once per entire test session |

### Markers

```python
@pytest.mark.smoke          # custom marker
@pytest.mark.e2e
@pytest.mark.skip(reason="WIP")
@pytest.mark.xfail(reason="Known bug")
def test_example():
    pass
```

Register in `pytest.ini` to avoid warnings:
```ini
[pytest]
markers =
    smoke: Smoke tests
    e2e: End-to-end tests
```

### Parametrize (Data-Driven)

```python
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (4, 5, 9),
])
def test_add(a, b, expected):
    assert a + b == expected
```

### Useful Pytest Flags

| Flag | Purpose |
|------|---------|
| `-v` | Verbose output |
| `-s` | Show print/stdout |
| `-x` | Stop on first failure |
| `-k "pattern"` | Run tests matching name pattern |
| `-m "marker"` | Run tests with specific marker |
| `--lf` | Re-run only last failed tests |
| `--ff` | Run failed first, then rest |
| `-n 4` | Parallel execution (4 workers, needs `pytest-xdist`) |
| `--html=report.html` | Generate HTML report |
| `--reruns 2` | Retry failed tests 2 times |
| `--timeout=120` | Timeout per test |
| `--cov=.` | Code coverage |

---

## 3. Playwright — Browser & Page Setup

### Three Ways to Get a Page

```python
# 1. Manual setup (full control)
def test_manual(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://example.com")
    # Don't forget to close!
    context.close()
    browser.close()

# 2. Built-in page fixture (auto-managed by pytest-playwright)
def test_auto(page):
    page.goto("https://example.com")

# 3. Built-in page fixture with type hint
from playwright.sync_api import Page
def test_typed(page: Page):
    page.goto("https://example.com")
```

### Launch Different Browsers

```python
# Chromium (default)
browser = playwright.chromium.launch(headless=False)

# Firefox
browser = playwright.firefox.launch(headless=False)

# WebKit (Safari engine)
browser = playwright.webkit.launch(headless=False)
```

### Browser → Context → Page Hierarchy

```
Browser
 └── Context (isolated session — cookies, storage, viewport)
      └── Page (a single tab)
```

---

## 4. Playwright — Locators

### Recommended Locators (Best → Acceptable)

| Locator | Example | When to Use |
|---------|---------|-------------|
| `get_by_role()` | `page.get_by_role("button", name="Login")` | Buttons, links, headings — **preferred** |
| `get_by_placeholder()` | `page.get_by_placeholder("email@example.com")` | Input fields with placeholder |
| `get_by_label()` | `page.get_by_label("Username:")` | Form fields with labels |
| `get_by_text()` | `page.get_by_text("Sign In")` | Text content |
| `locator()` (CSS) | `page.locator("#username")` | CSS selector — IDs, classes |
| `locator()` (XPath) | `page.locator("//div[@class='card']")` | Complex DOM queries |

### Real Examples from Codebase

```python
# Role-based
page.get_by_role("button", name="Login").click()
page.get_by_role("button", name="ORDERS").click()
page.get_by_role("combobox").select_option("consult")
page.get_by_role("link", name="Top").click()

# Placeholder
page.get_by_placeholder("email@example.com").fill("user@mail.com")
page.get_by_placeholder("enter your passsword").fill("pass123")

# Label
page.get_by_label("Username:").fill("rahulshettyacademy")
page.get_by_label("Password:").fill("learning")

# CSS selector
page.locator("#username").fill("rahulshettyacademy")
page.locator("#terms").check()
page.locator(".mt-4").text_content()
page.locator(".tagline").text_content()

# Text-based
page.get_by_text("Checkout").click()
```

### Filtering & Chaining Locators

```python
# Filter by text
page.locator("tr").filter(has_text=orderId).get_by_role("button", name="View").click()

# Filter cards
appCards = page.locator("app-card")
iphoneX = appCards.filter(has_text="iPhone X")
iphoneX.get_by_role("button", name="Add").click()

# nth element (0-based)
page.get_by_role("button", name="View").nth(0).click()
page.locator("th").nth(i)

# Count elements
count = page.locator("th").count()
```

---

## 5. Playwright — Assertions (expect)

```python
from playwright.sync_api import expect

# Visibility
expect(page.get_by_text("Error message")).to_be_visible()
expect(page.get_by_placeholder("Hide/Show")).to_be_hidden()

# Text content
expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
expect(frame.locator("body")).to_contain_text("Learning Journey")

# Count
expect(page.locator(".media")).to_have_count(2)

# Standard Python assert (for non-locator values)
assert price == "37"
assert message.__contains__("No Orders")
assert orderId == page.locator("tbody tr th").nth(0).text_content()
```

### expect vs assert

| | `expect()` | `assert` |
|--|-----------|----------|
| **Source** | Playwright library | Python built-in |
| **Auto-wait** | ✅ Yes — retries until timeout | ❌ No — instant check |
| **Use for** | Page elements / locators | Variables, API responses, strings |
| **Error messages** | Rich, descriptive | Basic |

---

## 6. Playwright — Actions

```python
# Navigate
page.goto("https://example.com")

# Type / Fill
page.locator("#username").fill("text")
page.get_by_placeholder("email").fill("user@mail.com")

# Click
page.get_by_role("button", name="Submit").click()

# Check / Uncheck
page.locator("#terms").check()
page.locator("#terms").uncheck()

# Select dropdown
page.get_by_role("combobox").select_option("consult")

# Hover
page.get_by_role("button", name="Mouse Hover").hover()

# Get text content
text = page.locator(".message").text_content()

# Screenshot
page.screenshot(path="screenshot.png")
```

---

## 7. Playwright — Waits & Auto-Wait

Playwright **auto-waits** for elements before performing actions (click, fill, etc.).

```python
# Explicit wait for element
page.wait_for_selector("#loading", state="hidden")

# Wait for URL
page.wait_for_url("**/dashboard")

# Wait for load state
page.wait_for_load_state("domcontentloaded")
page.wait_for_load_state("networkidle")

# Wait for timeout (avoid if possible)
page.wait_for_timeout(3000)   # 3 seconds
```

> 💡 **Tip:** Prefer `expect()` assertions over explicit waits — they auto-retry.

---

## 8. Playwright — Network Interception

### Mock a Request URL (Redirect)

```python
def interceptRequest(route):
    route.continue_(url="https://example.com/api/different-endpoint")

page.route("https://example.com/api/original-endpoint?id=*", interceptRequest)
```

### Mock a Response (Fake Data)

```python
def interceptResponse(route):
    route.fulfill(
        json={"data": [], "message": "No Orders"}
    )

page.route("https://example.com/api/orders/*", interceptResponse)
page.get_by_role("button", name="ORDERS").click()

message = page.locator(".mt-4").text_content()
assert "No Orders" in message
```

### Key Methods

| Method | Purpose |
|--------|---------|
| `route.continue_()` | Let request proceed (optionally modify URL/headers) |
| `route.fulfill()` | Return a fake response (mock) |
| `route.abort()` | Block the request entirely |

---

## 9. Playwright — API Testing

### Create API Request Context

```python
from playwright.sync_api import Playwright

api_context = playwright.request.new_context(
    base_url="https://rahulshettyacademy.com",
    ignore_https_errors=True
)
```

### Make API Calls

```python
# POST — Login
response = api_context.post(
    url="/api/ecom/auth/login",
    data={"userEmail": "user@mail.com", "userPassword": "pass123"}
)
token = response.json()["token"]

# POST — Create Order (with auth header)
response = api_context.post(
    url="/api/ecom/order/create-order",
    data={"orders": [{"country": "India", "productOrderedId": "abc123"}]},
    headers={
        "Authorization": token,
        "Content-type": "application/json"
    }
)
order_id = response.json()["orders"][0]

# Assert response
assert response.status == 200
assert response.json()["message"] == "Order Placed Successfully"
```

### API + UI Hybrid Testing Pattern

```python
def test_e2e(playwright, browser_instance, credentials):
    # Step 1: Create order via API
    orderId = APIUtils.createOrder(playwright, userCredentials=credentials)

    # Step 2: Verify in UI
    loginPage = LoginPage(browser_instance)
    loginPage.navigate()
    dashboardPage = loginPage.login(credentials)
    orderDetailsPage = dashboardPage.click_order_button()
    orderDetailsPage.clickViewByOrderId(orderId)

    expect(browser_instance.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
```

---

## 10. Playwright — iFrames, Dialogs, Child Windows

### iFrames

```python
# Locate the iframe, then interact within it
frame = page.frame_locator("#courses-iframe")
frame.locator("a[href='/learning-paths']").nth(0).click()
expect(frame.locator("body")).to_contain_text("Learning Journey")
```

### Dialogs (Alerts / Confirms)

```python
# Accept dialog when it appears
page.on("dialog", lambda dialog: dialog.accept())
page.get_by_role("button", name="Confirm").click()

# Dismiss dialog
page.on("dialog", lambda dialog: dialog.dismiss())

# Get dialog message
def handle_dialog(dialog):
    print(dialog.message)
    dialog.accept()

page.on("dialog", handle_dialog)
```

### Child Windows / Tabs (Popups)

```python
with page.expect_popup() as popup_info:
    page.locator(".blinkingText").click()   # triggers new tab
    child_page = popup_info.value

print(child_page.title())
text = child_page.locator(".red").text_content()
email = text.split("at")[1].split("with")[0].strip()
assert email == "mentor@rahulshettyacademy.com"
```

---

## 11. Playwright — Tracing & Debugging

### Enable Tracing (in conftest.py)

```python
# Start tracing
context.tracing.start(screenshots=True, snapshots=True, sources=True)

# ... run test ...

# Stop and save trace
context.tracing.stop(path="traces/trace_test_name.zip")
```

### View Trace

```powershell
playwright show-trace traces/trace_test_name.zip
```

### CLI Tracing Flag (custom)

```powershell
# Enable
python -m pytest --custom-tracing on

# Disable
python -m pytest --custom-tracing off
```

### Debugging Tips

```powershell
# Pause execution on failure and drop into debugger
python -m pytest --pdb

# Verbose + show prints
python -m pytest -v -s

# Headed mode (see browser)
python -m pytest --headed

# Slow motion (milliseconds)
# In code: playwright.chromium.launch(slow_mo=500)
```

---

## 12. Playwright — Session / Cookie Injection

Skip login UI by injecting auth tokens directly:

```python
def test_inject_session(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Get token via API
    token = APIUtils.getToken(playwright, userCredentials={...})

    # Inject into browser localStorage BEFORE navigating
    page.add_init_script(f"""localStorage.setItem("token", "{token}")""")

    # Now navigate — user is already logged in
    page.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")
    expect(page.get_by_text("Your Orders")).to_be_visible()
```

> 💡 **Why?** Saves time by avoiding login UI for every test. Great for tests that don't test login itself.

---

## 13. Page Object Model (POM)

### Pattern

Each page in the app gets its own class with locators and action methods.  
Methods return the **next page object** for chaining.

### LoginPage

```python
class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self, credentials):
        self.page.get_by_placeholder("email@example.com").fill(credentials["username"])
        self.page.get_by_placeholder("enter your passsword").fill(credentials["password"])
        self.page.get_by_role("button", name="Login").click()
        return DashboardPage(self.page)   # ← returns next page
```

### DashboardPage

```python
class DashboardPage:
    def __init__(self, page):
        self.page = page

    def click_order_button(self):
        self.page.get_by_role("button", name="Orders").click()
        return OrdersPage(self.page)      # ← returns next page
```

### OrdersPage

```python
class OrdersPage:
    def __init__(self, page):
        self.page = page

    def clickViewByOrderId(self, orderId):
        self.page.locator("tr").filter(has_text=orderId).get_by_role("button", name="View").click()
```

### Usage in Test

```python
loginPage = LoginPage(browser_instance)
loginPage.navigate()
dashboardPage = loginPage.login(credentials)          # returns DashboardPage
orderDetailsPage = dashboardPage.click_order_button()  # returns OrdersPage
orderDetailsPage.clickViewByOrderId(orderId)
```

---

## 14. Data-Driven Testing

### JSON Data File

```json
{
  "credentials": [
    { "username": "user1@mail.com", "password": "Pass@123" },
    { "username": "user2@mail.com", "password": "Pass@456" }
  ]
}
```

### Load & Parametrize

```python
import json
import pytest

with open("Playwright/Framework/Data/credentials.json") as f:
    test_data = json.load(f)
    test_credentials = test_data["credentials"]

@pytest.mark.parametrize("creds", test_credentials)
def test_login(browser_instance, creds):
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    login_page.login(creds)
```

> Each dict in the list becomes a separate test case automatically.

---

## 15. conftest.py — Fixtures & Hooks

### Purpose

- Shared fixtures across test files (no import needed)
- Custom CLI options
- Pytest hooks (modify behavior)
- Auto-discovered by pytest

### Key Patterns Used

```python
# Custom CLI options
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--custom-tracing", action="store", default="on", choices=["on", "off"])

# Fixture with yield (setup + teardown)
@pytest.fixture(scope="function")
def browser_instance(playwright, request):
    browser_name = request.config.getoption("--browser_name")

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield page            # ← test runs here

    context.tracing.stop(path="traces/trace.zip")
    context.close()       # ← teardown
    browser.close()
```

### Fixture Dependency Chain

```
pytest-playwright provides `playwright` fixture
    → conftest.py uses it in `browser_instance` fixture
        → test function receives `browser_instance` as argument
```

---

## 16. Pytest CLI Commands — Quick Reference

### Run Tests

```powershell
# All tests
python -m pytest

# Specific file
python -m pytest Playwright/Framework/Tests/test_e2eFlowHybridFramework.py

# Specific test function
python -m pytest path/to/test_file.py::test_function_name

# By marker
python -m pytest -m smoke
python -m pytest -m "smoke or e2e"
python -m pytest -m "smoke and not slow"

# By keyword in test name
python -m pytest -k "login"
```

### Reporting & Coverage

```powershell
# HTML report
python -m pytest --html=report.html --self-contained-html

# Code coverage
python -m pytest --cov=. --cov-report=html

# Allure report
python -m pytest --alluredir=allure-results
allure serve allure-results
```

### Execution Control

```powershell
# Parallel (4 workers)
python -m pytest -n 4

# Stop on first failure
python -m pytest -x

# Retry failed tests
python -m pytest --reruns 2 --reruns-delay 1

# Re-run only last failed
python -m pytest --lf

# Run failed first
python -m pytest --ff

# Timeout per test
python -m pytest --timeout=120
```

### Debugging

```powershell
# Verbose + show prints
python -m pytest -v -s

# Drop into debugger on failure
python -m pytest --pdb

# Show local variables on failure
python -m pytest -l

# Show 10 slowest tests
python -m pytest --durations=10
```

### Browser Options

```powershell
# Choose browser
python -m pytest --browser_name=chrome
python -m pytest --browser_name=firefox
python -m pytest --browser_name=webkit

# Headed mode
python -m pytest --headed

# Tracing
python -m pytest --custom-tracing on
```

### Combined (Common Scenarios)

```powershell
# Local development
python -m pytest -v -s --headed

# CI/CD pipeline
python -m pytest -n 4 --html=report.html --cov=. --reruns 2

# Smoke suite with report
python -m pytest -m smoke -v --html=smoke_report.html

# Debug a specific failing test
python -m pytest path/to/test.py::test_name -v -s --headed --pdb
```

### Playwright CLI

```powershell
# Install browsers
playwright install

# View trace file
playwright show-trace traces/trace_test_name.zip

# Code generation (record actions)
playwright codegen https://example.com
```

---

*Last Updated: February 2026*
