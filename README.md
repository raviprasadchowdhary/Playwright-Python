# PythonPlaywright

A comprehensive Python testing framework demonstrating **Playwright automation**, **API testing**, **E2E testing**, and **pytest fundamentals**. This project includes practical examples of browser automation, network interception, and test automation best practices.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Sections](#project-sections)
- [Running Tests](#running-tests)
- [Key Features](#key-features)

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
Basic Playwright tests covering:
- **Core Locators**: Using CSS selectors, role-based, and label-based locators
- **Browser Navigation**: Different ways to navigate pages
- **Browser Variants**: Testing with Firefox browser
- **Window/Tab Handling**: Managing multiple windows and tabs
- **Form Filling & Interactions**: Login flows and product cart operations

**Example Test:**
```python
# test_coreLocators.py - Demonstrates different locator strategies
page.get_by_label("Username:").fill("username")
page.get_by_role("button", name="Sign In").click()
expect(page.get_by_text("Success")).to_be_visible()
```

### 2. **API Testing**
Test REST API endpoints programmatically:
- **Authentication**: Getting auth tokens
- **CRUD Operations**: Creating, reading, updating, deleting resources
- **Response Validation**: Verifying status codes and response bodies
- **Test Flow**: Login → Add to Cart → Create Order

**Example Test:**
```python
# test_API.py - API endpoint testing
authToken = getAuthToken(playwright)
response = addToCartZaraCoat3(playwright)
assert response.status == 200
assert response.json()["message"] == "Product Added To Cart"
```

### 3. **End-to-End Testing (E2E)**
Hybrid E2E tests combining UI and API operations:
- **Browser Launch**: Launching Chromium browser
- **UI Interactions**: Login through the web interface
- **API Integration**: Creating orders via API
- **Verification**: Validating results through UI

**Example Flow:**
```
1. Launch browser
2. Navigate to login page
3. Fill credentials and login
4. Create order via API call
5. Verify order appears in UI
6. Cleanup
```

### 4. **Testing Framework (Advanced)**
A structured testing framework using **Page Object Model (POM)**:
- **LoginPage**: Handles authentication
- **DashboardPage**: Dashboard interactions
- **OrdersPage**: Order management
- **APIUtils**: Shared API utilities
- **Test Data**: JSON-driven test cases with parametrization

**Benefits:**
- Maintainable code with separation of concerns
- Reusable page objects
- Parametrized tests with multiple credentials
- Centralized test data management

### 5. **Network Interception**
Advanced Playwright features for network manipulation:
- **Session Cookie Injection**: Bypassing login by injecting auth tokens
- **Network Mocking**: Intercepting and modifying requests
- **Response Mocking**: Simulating API responses
- **Unauthorized Access Testing**: Handling authentication scenarios

**Example Use Case:**
```python
# Inject session token to skip login
api_utils = APIUtils()
token = api_utils.getToken(playwright, userCredentials=credentials)
page.add_init_script(f'localStorage.setItem("token", "{token}")')
page.goto("dashboard-url")  # No login needed!
```

### 6. **Pytest Basics**
Understanding pytest framework and best practices:
- **Fixtures**: Function, module, class, and session-scoped fixtures
- **Conftest**: Shared configurations across tests
- **Setup/Teardown**: Test initialization and cleanup
- **Parametrization**: Running tests with multiple inputs
- **Scope Management**: Understanding fixture lifecycles

**Example Fixture:**
```python
# conftest.py - Fixture with setup and teardown
@pytest.fixture(scope="module")
def setup_module():
    print("Setting up module")
    yield
    print("Tearing down module")
```

### 7. **Python Basics**
Foundational Python concepts:
- **Data Types**: Integers, floats, strings, booleans, complex numbers
- **Collections**: Lists, tuples, dictionaries
- **Control Flow**: If/elif/else, for loops, while loops
- **Functions**: Defining and calling functions
- **File Operations**: Reading and writing files
- **OOPS**: Classes, inheritance, polymorphism

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

**Beginners:**
1. Start with `PythonBasics/` to understand Python fundamentals
2. Move to `PytestBasics/` to learn pytest framework
3. Explore `Playwright/part1/` for basic browser automation

**Intermediate:**
4. Study `Playwright/Framework/` to understand Page Object Model
5. Work through `Playwright/E2E/` for end-to-end scenarios

**Advanced:**
6. Dive into `Playwright/NetworkInterception/` for advanced features
7. Explore `Playwright/API_Testing/` for API automation
8. Analyze the hybrid approach in `test_e2eFlowHybridFramework.py`

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
