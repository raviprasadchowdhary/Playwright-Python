# PythonPlaywright

A comprehensive Python testing framework demonstrating **Playwright automation**, **API testing**, **E2E testing**, and
**pytest fundamentals**. This project includes practical examples of browser automation, network interception, and test
automation best practices with a focus on real-world testing scenarios.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Sections](#project-sections)
- [Running Tests](#running-tests)
- [Key Features](#key-features)
- [Learning Path](#learning-path)
- [Test Website](#test-website)

## 🎯 Project Overview

This repository is a learning resource and practical guide for:

- **Playwright Testing**: Browser automation using Playwright Python SDK
- **API Testing**: Automated testing of REST APIs
- **E2E Testing**: End-to-end testing workflows combining UI and API
- **Pytest Framework**: Understanding pytest fixtures, configurations, and best practices
- **Python Fundamentals**: Core Python concepts and OOPS principles

## 📁 Project Structure

```
PythonPlaywright/
├── Playwright/                          # Main Playwright automation folder
│   ├── API_Testing/                     # API testing examples
│   │   ├── test_API.py                  # API test cases
│   │   └── helper.py                    # API helper functions
│   ├── E2E/                             # End-to-end testing
│   │   └── test_e2eFlowHybrid.py        # Hybrid E2E test (UI + API)
│   ├── Framework/                       # Advanced testing framework
│   │   ├── PageObjects/                 # Page Object Model implementation
│   │   │   ├── loginPage.py
│   │   │   ├── dashboardPage.py
│   │   │   └── ordersPage.py
│   │   ├── Tests/                       # Test files using framework
│   │   │   └── test_e2eFlowHybridFramework.py
│   │   ├── Data/                        # Test data
│   │   │   └── credentials.json
│   │   └── conftest.py                  # Pytest configuration for framework tests
│   ├── NetworkInterception/             # Network mocking and interception
│   │   ├── test_injectSessionCookiesIntoBrowserAtRunTime.py
│   │   ├── test_networkInterception_mockRequest_unauthorizedAccess.py
│   │   └── test_networkInterception_mockresponse_noOrders.py
│   ├── part1/                           # Basic Playwright tests
│   │   ├── test_coreLocators.py         # CSS, role, label-based locators
│   │   ├── test_differentWaysToGoToPage.py
│   │   ├── test_firefoxBrowser.py
│   │   ├── test_handleChildWindowsAndTabs.py
│   │   └── test_loginAndAddProductsToCart.py
│   ├── Part2/                           # Advanced validation tests
│   │   └── test_moreValidations.py
│   └── conftest.py                      # Global pytest configuration
├── PytestBasics/                        # Pytest learning examples
│   ├── ConfTest/                        # Conftest and fixtures examples
│   │   ├── conftest.py
│   │   ├── test_pyTestValidation1.py
│   │   └── test_pyTestValidation2.py
│   └── FixtureFunctionModule/           # Different fixture scopes
│       ├── fixture_scope_function.py
│       └── fixture_scope_module.py
├── PythonBasics/                        # Python fundamentals
│   ├── demo.py
│   ├── rough.py
│   ├── DataTypes/                       # Python data types
│   │   ├── data_type_integer_float_complex_boolean_string.py
│   │   ├── data_types.py
│   │   ├── dictionary.py
│   │   ├── list.py
│   │   └── tuple.py
│   ├── FileOperations/                  # File I/O operations
│   │   ├── read_write.py
│   │   ├── read_write2.py
│   │   └── test files
│   ├── Functions/                       # Function definitions and calls
│   │   └── functions.py
│   ├── Loops/                           # Loop constructs
│   │   ├── for.py
│   │   ├── if_elif_else.py
│   │   └── while.py
│   └── OOPS/                            # Object-Oriented Programming
│       ├── oops.py
│       ├── parent.py
│       └── child.py
├── utils/                               # Shared utilities
│   └── apiBase.py                       # API utility functions
├── prerequisites.txt                    # Development environment setup guide
└── README.md                            # This file
```

## 📦 Prerequisites

Before setting up your development environment, ensure you have:

1. **Operating System**: Windows 10+, macOS Catalina+, or a recent Linux distribution
2. **Python**: Version 3.8 or later (check with `python --version`)
3. **pip**: Python package manager (usually comes with Python)
4. **Git**: For version control (optional but recommended)
5. **Virtual Environment**: Recommended to use `venv`

For detailed prerequisites, see [prerequisites.txt](prerequisites.txt)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/PythonPlaywright.git
cd PythonPlaywright
```

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install pytest playwright requests
playwright install
```

For detailed setup instructions, refer to [prerequisites.txt](prerequisites.txt)

## 🧪 Project Sections

### 1. **Playwright Basics (part1)**

Basic Playwright tests covering core automation concepts:

- **Core Locators** (`test_coreLocators.py`): CSS selectors, role-based, and label-based locators
- **Browser Navigation** (`test_differentWaysToGoToPage.py`): Different approaches to navigate pages (manual vs. fixture-based)
- **Browser Variants** (`test_firefoxBrowser.py`): Testing with Firefox browser instead of Chromium
- **Window/Tab Handling** (`test_handleChildWindowsAndTabs.py`): Managing multiple windows, tabs, and child pages
- **Form Filling & Interactions** (`test_loginAndAddProductsToCart.py`): Login flows and adding products to cart

**Key Techniques:**
- Using Playwright's built-in page fixture for automatic browser management
- Locating elements by role, label, and CSS selectors
- Handling dynamic content and assertions with `expect()`
- Extracting text content from elements

**Example Test:**

```python
# test_coreLocators.py - Demonstrates different locator strategies
page.get_by_label("Username:").fill("rahulshettyacademy")
page.get_by_role("combobox").select_option("consult")
page.get_by_role("button", name="Sign In").click()
expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
```

### 2. **Advanced Validations (Part2)**

Advanced testing scenarios and validations:

- **Placeholder Locators**: Testing elements with placeholder attributes
- **Dialog/Alert Handling**: Handling JavaScript alerts and confirm dialogs
- **Iframe Handling**: Working with iframes and frames within pages
- **Table Content Validation**: Verifying table data and content
- **Multiple Test Scenarios**: Various validation techniques for complex UI interactions

**Example Test:**

```python
# test_moreValidations.py - Handling dialogs and iframes
page.on("dialog", lambda dialog: dialog.accept())
page.get_by_role("button", name="Confirm").click()

# Working with iframes
frame = page.frame_locator("#courses-iframe")
frame.locator("a").nth(0).click()
```

### 3. **API Testing**

REST API testing using Playwright's request context:

- **Authentication**: Getting auth tokens via login API
- **CRUD Operations**: Creating orders, adding to cart via API endpoints
- **Response Validation**: Verifying status codes, response bodies, and message content
- **Reusable Helpers**: API helper functions for common operations

**Files:**
- `test_API.py`: API test cases for authentication, cart operations, and order creation
- `helper.py`: Reusable API request context and helper functions

**Key Operations:**
- `getAuthToken()`: Authenticate and retrieve auth token
- `addToCartZaraCoat3()`: Add specific product to cart
- `createOrder()`: Create order and get order ID

**Example Test:**

```python
# test_API.py - API endpoint testing
def test_getAuthToken(playwright):
    authToken = getAuthToken(playwright)
    assert authToken is not None

def test_createOrder(playwright):
    response = createOrder(playwright)
    assert response.status == 201
    assert response.json()["message"] == "Order Placed Successfully"
```

### 4. **End-to-End Testing (E2E)**

Hybrid E2E tests combining UI interactions with API operations:

- **Manual Flow** (`test_e2eFlowHybrid.py`): Manual browser setup with API integration
- **Login via UI**: Authenticating through web interface
- **API Integration**: Creating orders via API after login
- **Verification**: Validating orders appear in the UI

**Example Flow:**

```
1. Launch Chromium browser (non-headless for visibility)
2. Navigate to login page
3. Fill credentials and authenticate via UI
4. Create order using API call
5. Navigate to Orders page
6. Verify order ID matches the one created via API
7. Click View to see order details
```

**Key Assertions:**
```python
assert orderId == page.locator("tbody tr th").nth(0).text_content()
```

### 5. **Testing Framework (Advanced)**

A production-ready testing framework using **Page Object Model (POM)**:

**Structure:**
- **PageObjects/**: Reusable page object classes
  - `common.py`: Common utilities for browser creation
  - `loginPage.py`: Login page interactions
  - `dashboardPage.py`: Dashboard operations
  - `ordersPage.py`: Orders page interactions
- **Tests/**: Test files using the framework
  - `test_e2eFlowHybridFramework.py`: E2E test with parametrized credentials
- **Data/**: Test data in JSON format
  - `credentials.json`: Multiple user credentials for parametrized tests
- **conftest.py**: Pytest configuration and fixtures

**Page Object Classes:**

```python
# LoginPage - Handles authentication
class LoginPage:
    def __init__(self, page):
        self.page = page
    
    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")
    
    def login(self, test_credentials_list):
        self.page.get_by_placeholder("email@example.com").fill(test_credentials_list["username"])
        self.page.get_by_placeholder("enter your passsword").fill(test_credentials_list["password"])
        self.page.get_by_role("button", name="Login").click()
        return DashboardPage(self.page)

# DashboardPage - Dashboard interactions
class DashboardPage:
    def __init__(self, page):
        self.page = page
    
    def click_order_button(self):
        self.page.get_by_role("button", name="Orders").click()
        return OrdersPage(self.page)

# OrdersPage - Order management
class OrdersPage:
    def clickViewByOrderId(self, orderId):
        self.page.locator("tr").filter(has_text=orderId).get_by_role("button", name="View").click()
```

**Test Data (credentials.json):**
```json
{
  "credentials": [
    {
      "username": "RahulChowdhary@gmailc.om",
      "password": "Rahul@123"
    },
    {
      "username": "RohanChowdhary@gmailc.om",
      "password": "Rohan@123"
    }
  ]
}
```

**Parametrized Test:**
```python
@pytest.mark.smoke
@pytest.mark.e2e
@pytest.mark.parametrize("test_credentials_list", test_credentials)
def test_e2eTest_createOrderAndVerify(playwright, browser_instance, test_credentials_list):
    # Create order via API
    orderId = APIUtils.createOrder(playwright, userCredentials=test_credentials_list)
    
    # Verify in UI
    loginPage = LoginPage(browser_instance)
    loginPage.navigate()
    dashboardPage = loginPage.login(test_credentials_list)
    orderDetailsPage = dashboardPage.click_order_button()
    orderDetailsPage.clickViewByOrderId(orderId)
    
    expect(browser_instance.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
```

**Benefits:**
- Maintainable code with separation of concerns
- Reusable page objects across multiple tests
- Parametrized tests for multiple user scenarios
- Centralized test data management
- Custom pytest fixtures for browser configuration

### 6. **Network Interception & Advanced Features**

Advanced Playwright capabilities for network manipulation and testing:

**Session Cookie Injection** (`test_injectSessionCookiesIntoBrowserAtRunTime.py`):
- Bypassing login by injecting auth tokens into browser storage
- Useful for testing authenticated pages without UI login
- Saves time by skipping login UI for each test

```python
api_utils = APIUtils()
token = api_utils.getToken(playwright, userCredentials=credentials)
page.add_init_script(f'localStorage.setItem("token", "{token}")')
page.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")
```

**Request Mocking** (`test_networkInterception_mockRequest_unauthorizedAccess.py`):
- Intercepting and modifying HTTP requests
- Testing unauthorized access scenarios
- Simulating different API responses

```python
def interceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6937107f32ed86587126a601")

page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", interceptRequest)
```

**Response Mocking** (`test_networkInterception_mockresponse_noOrders.py`):
- Intercepting and replacing API responses
- Testing UI behavior with mocked data
- Simulating "no orders" or other empty states

```python
def interceptResponse(route):
    route.fulfill(json={"data": [], "message": "No Orders"})

page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", interceptResponse)
```

### 7. **Pytest Basics & Fixtures**

Understanding pytest framework and fixture scopes:

**Files:**
- `ConfTest/conftest.py`: Demonstrates all fixture scopes
- `ConfTest/test_pyTestValidation1.py`: Tests using fixtures
- `ConfTest/test_pyTestValidation2.py`: Additional fixture examples
- `FixtureFunctionModule/`: Examples of function and module-scoped fixtures

**Fixture Scopes:**

```python
# conftest.py - Different fixture scopes

@pytest.fixture(scope="session")
def setup_session():
    print("\nSetup: Executing before the test session")
    yield
    print("\nTeardown: Executing after the test session")

@pytest.fixture(scope="module")
def setup_module():
    print("\nSetup: Executing before the test module")
    yield
    print("\nTeardown: Executing after the test module")

@pytest.fixture(scope="function")
def setup_function():
    print("\nSetup: Executing before each test function")
    yield
    print("\nTeardown: Executing after each test function")

@pytest.fixture(scope="class")
def setup_class():
    print("\nSetup: Executing before the test class")
    yield
    print("\nTeardown: Executing after the test class")
```

**Test Usage:**
```python
def test_validation1(setup_session, setup_module, setup_function):
    print("Executing test validation1")
    assert True

class TestValidationClass:
    def test_validation3(self, setup_class):
        print("Executing test validation3")
        assert True
```

**Fixture Features:**
- Setup and teardown logic
- Resource initialization and cleanup
- Scope management (session, module, function, class)
- Fixture dependency injection
- Parametrization with fixtures

### 8. **Python Fundamentals**

Core Python concepts and OOPS principles:

**Data Types** (`DataTypes/`):
- Integers, floats, complex numbers, booleans
- Strings and their operations
- Lists, tuples, and dictionaries
- Type conversions and operations

**Control Flow** (`Loops/`):
- If/elif/else conditional statements
- For loops and iteration
- While loops and loop control
- Break, continue, and pass statements

**Functions** (`Functions/`):
- Function definition and calling
- Parameters and arguments
- Return values
- Scope and namespaces

**File Operations** (`FileOperations/`):
- Reading files
- Writing files
- File handling best practices
- Working with different file formats

**Object-Oriented Programming** (`OOPS/`):
- Classes and objects
- Inheritance and polymorphism
- Encapsulation
- Method overriding
- Parent-child class relationships

**String Operations** (`String/`):
- String creation and manipulation
- String methods and formatting
- Regular expressions basics
- String indexing and slicing

## 🛠️ Utilities

**API Utilities:**
- `utils/apiBase.py`: Basic API utilities with hardcoded credentials
- `utils/apiBaseFramework.py`: Framework-friendly API utilities with parameterized credentials

**APIUtils Features:**
- `getToken()`: Retrieve authentication token
- `createOrder()`: Create orders via API
- Integration with Playwright's request context
- Support for parametrized user credentials

## ▶️ Running Tests

### Run All Tests

```bash
pytest
```

### Run Specific Directory

```bash
pytest Playwright/part1/
pytest Playwright/API_Testing/
pytest Playwright/Framework/Tests/
```

### Run Specific Test File

```bash
pytest Playwright/part1/test_coreLocators.py
```

### Run Specific Test

```bash
pytest Playwright/part1/test_coreLocators.py::test_core_locators
```

### Run with Verbose Output

```bash
pytest -v
```

### Run with Detailed Output

```bash
pytest -vv -s
```

### Run Playwright Tests with Headed Browser

```bash
# Tests run with visible browser (not headless)
pytest Playwright/E2E/ -v
```

### Generate HTML Report

```bash
pip install pytest-html
pytest --html=report.html --self-contained-html
```

### Run Tests in Parallel (pytest-xdist)

**Install pytest-xdist plugin:**

```bash
pip install pytest-xdist
```

**Run tests in parallel using multiple workers:**

```bash
# Run tests using 4 workers (processes)
pytest -n 4

# Run tests using auto-detection of CPU count
pytest -n auto

# Run tests with 2 workers and verbose output
pytest -n 2 -v

# Run specific directory in parallel
pytest Playwright/part1/ -n auto

# Run with verbose output and parallel execution
pytest -n auto -v
```

**Benefits of Parallel Testing:**
- Significantly faster test execution
- Better resource utilization
- Ideal for large test suites
- Reduces overall CI/CD pipeline time

**Example Usage:**

```bash
# Run all tests in parallel with auto-detected CPU count
pytest -n auto

# Run Framework tests in parallel with 4 workers
pytest Playwright/Framework/Tests/ -n 4 -v

# Run API tests in parallel with detailed output
pytest Playwright/API_Testing/ -n auto -vv
```

**Notes on Parallel Execution:**
- Each worker runs in a separate process
- Tests must be independent and not share state
- Network interception tests work well with parallel execution
- Some fixtures may need adjustment for parallel runs

### Combine Parallel Execution with Report Generation

```bash
# Run tests in parallel and generate HTML report
pytest -n auto --html=report.html --self-contained-html

# Run with multiple workers, verbose output, and report
pytest -n 4 -v --html=report.html --self-contained-html

# Run API tests in parallel with comprehensive reporting
pytest Playwright/API_Testing/ -n auto -v --html=api_report.html --self-contained-html
```

## 📊 Report Generation with pytest-html

**Install pytest-html plugin:**

```bash
python -m pip install pytest-html
```

**Generate basic HTML report:**

```bash
pytest --html=report.html
```

**Generate self-contained HTML report (includes all CSS/JS inline):**

```bash
pytest --html=report.html --self-contained-html
```

**Generate report with additional options:**

```bash
# Report with detailed output
pytest --html=report.html --self-contained-html -v

# Report with screenshot capture (if available)
pytest --html=report.html --self-contained-html --screenshot=on

# Report with custom name and timestamp
pytest --html=report_$(date +%Y%m%d_%H%M%S).html --self-contained-html
```

**Report Features:**
- Clear test execution summary
- Pass/fail/skip/error statistics
- Individual test details with duration
- Error messages and stack traces
- HTML format viewable in any browser
- Self-contained option for easy sharing

**Example Report Commands by Test Type:**

```bash
# Framework tests with HTML report
pytest Playwright/Framework/Tests/ --html=framework_report.html --self-contained-html -v

# API tests with detailed report
pytest Playwright/API_Testing/ --html=api_report.html --self-contained-html -vv

# E2E tests with parallel execution and report
pytest Playwright/E2E/ -n auto --html=e2e_report.html --self-contained-html -v

# All tests with parallel execution, verbose output, and report
pytest -n auto --html=complete_report.html --self-contained-html -v
```

## 🌟 Key Features

✅ **Multiple Testing Approaches**

- Unit testing with Playwright
- API testing with requests
- End-to-end testing combining UI and API
- Network interception and mocking

✅ **Best Practices**

- Page Object Model for maintainability
- Parametrized tests for multiple scenarios
- Fixture-based test setup/teardown
- Centralized test data management

✅ **Advanced Concepts**

- Browser automation with different browsers
- Network mocking and request interception
- Session management and authentication
- API token injection into browser context

✅ **Comprehensive Coverage**

- Python fundamentals to advanced concepts
- Pytest framework understanding
- Real-world testing scenarios
- Error handling and validations

## 📚 Learning Path

This project is organized from beginner to advanced concepts. Follow this progression:

**Phase 1: Python Fundamentals (PythonBasics/)**

Start here if you're new to Python:
1. `DataTypes/` - Understand integers, floats, strings, lists, tuples, dictionaries
2. `Loops/` - Learn if/elif/else, for loops, while loops
3. `Functions/` - Master function definitions and calls
4. `String/` - String manipulation and methods
5. `FileOperations/` - File I/O operations
6. `OOPS/` - Classes, inheritance, and polymorphism concepts

**Phase 2: Pytest Framework (PytestBasics/)**

Understanding testing framework:
1. `ConfTest/conftest.py` - Learn about pytest fixtures and configurations
2. `ConfTest/test_pyTestValidation1.py` - Fixtures in action with different scopes
3. `FixtureFunctionModule/` - Understand function and module-scoped fixtures
4. Understand fixture lifecycle, setup/teardown patterns

**Phase 3: Playwright Basics (Playwright/part1/)**

Learn browser automation fundamentals:
1. `test_coreLocators.py` - Master different locator strategies (role, label, CSS)
2. `test_differentWaysToGoToPage.py` - Understand fixture-based page management vs manual setup
3. `test_firefoxBrowser.py` - Launch and use different browser engines
4. `test_handleChildWindowsAndTabs.py` - Handle multiple windows and tabs
5. `test_loginAndAddProductsToCart.py` - Real-world form filling and interactions

**Phase 4: Advanced Validations (Playwright/Part2/)**

Master advanced testing scenarios:
1. `test_moreValidations.py` - Placeholder locators, dialogs, iframes, table validation
2. Learn handling JavaScript dialogs and confirm buttons
3. Master iframe/frame navigation

**Phase 5: API Testing (Playwright/API_Testing/)**

Automated API testing:
1. `helper.py` - Understand helper functions and API request context
2. `test_API.py` - Test authentication, cart operations, order creation
3. Learn API status code validation
4. Master response body assertions

**Phase 6: End-to-End Testing (Playwright/E2E/)**

Combining UI and API:
1. `test_e2eFlowHybrid.py` - Manual E2E flow: UI login + API order creation
2. Understand the hybrid approach
3. Learn assertion and verification in E2E tests

**Phase 7: Testing Framework with POM (Playwright/Framework/)**

Production-ready testing patterns:
1. `PageObjects/common.py` - Browser and context creation utilities
2. `PageObjects/loginPage.py` - Page object for login interactions
3. `PageObjects/dashboardPage.py` - Dashboard page object
4. `PageObjects/ordersPage.py` - Orders page object
5. `Tests/conftest.py` - Framework-specific fixtures and browser configuration
6. `Tests/test_e2eFlowHybridFramework.py` - Parametrized tests using POM and JSON data
7. `Data/credentials.json` - Parametrized test data

**Phase 8: Advanced Features (Playwright/NetworkInterception/)**

Master advanced automation:
1. `test_injectSessionCookiesIntoBrowserAtRunTime.py` - Session token injection
2. `test_networkInterception_mockRequest_unauthorizedAccess.py` - Request mocking
3. `test_networkInterception_mockresponse_noOrders.py` - Response mocking
4. Learn network interception patterns for testing edge cases

## 🔗 Test Website

Most tests interact with:

- **URL**: https://rahulshettyacademy.com/
- **Practice Site**: Login page and e-commerce platform for learning

## 💡 Tips

- Always run tests in a virtual environment
- Use parametrization for testing multiple scenarios
- Leverage fixtures to reduce code duplication
- Follow Page Object Model for UI testing
- Add meaningful assertions and error messages
- Keep test data separate from test logic

## 📝 Notes

- Tests use `pytest` for test execution and assertions
- Playwright is used for browser automation
- Some tests may require internet connectivity
- Tests are designed for learning and demonstration purposes

## 🤝 Contributing

Feel free to enhance this project by:

- Adding more test examples
- Improving documentation
- Adding new automation scenarios
- Fixing bugs or improving code quality

---

**Happy Testing! 🎉**
