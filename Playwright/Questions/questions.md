# Python & Pytest Interview Questions & Answers

## 1. What is the difference between a list and a tuple?

**Answer:**

**Key Differences:**

| Feature | List | Tuple |
|---------|------|-------|
| **Mutability** | Mutable (can be modified) | Immutable (cannot be changed) |
| **Syntax** | Square brackets `[]` | Parentheses `()` |
| **Performance** | Slower | Faster (optimized) |
| **Use Case** | Dynamic data that changes | Fixed data like coordinates, config |

**Code Example:**
```python
# Lists - Mutable
my_list = [1, 2, 3, 4]
my_list[0] = 10  # Can be modified
my_list.append(5)  # Can add elements
print(my_list)  # Output: [10, 2, 3, 4, 5]

# Tuples - Immutable
my_tuple = (1, 2, 3, 4)
# my_tuple[0] = 10  # This will raise TypeError
# my_tuple.append(5)  # This will raise AttributeError
print(my_tuple)  # Output: (1, 2, 3, 4)
```

---

## 2. What are Python's built-in data types?

**Answer:**
Python has several built-in data types organized by category:

- **Numeric Types:** `int`, `float`, `complex`
- **Sequence Types:** `list`, `tuple`, `range`
- **Text Type:** `str`
- **Mapping Type:** `dict`
- **Set Types:** `set`, `frozenset`
- **Boolean Type:** `bool`
- **Binary Types:** `bytes`, `bytearray`, `memoryview`

**Code Snippet:**
```python
# Numeric Types
integer = 42
floating_point = 3.14
complex_num = 3 + 4j

# Sequence Types
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3)
my_range = range(0, 5)

# Text Type
my_string = "Hello, Python!"

# Mapping Type
my_dict = {'name': 'Rahul', 'age': 25, 'city': 'Bangalore'}

# Set Types
my_set = {1, 2, 3, 4, 5}
my_frozenset = frozenset([1, 2, 3])

# Boolean Type
is_true = True
is_false = False

# Binary Types
my_bytes = b"Hello"
my_bytearray = bytearray(b"Hello")
```

---

## 3. How do you implement inheritance and super() keyword in Python?

**Answer:**
- Use `class Child(Parent):` to inherit from a parent class
- `super().__init__()` calls the parent class's methods and allows method overriding while accessing parent functionality

**Code Snippet from Codebase:**

```python
# Parent class (from PythonBasics/OOPS/parent.py)
class BaseCarModel:
    price = 1000000  # base price of the car model

    def __init__(self, model_name, year):
        self.model_name = model_name
        self.year = year

    def display_info(self):
        return f"Model: {self.model_name}; Year: {self.year}"

    def get_price(self):
        return self.price

# Child class (from PythonBasics/OOPS/child.py)
class DeluxeCarModel(BaseCarModel):
    deluxe_price = 200000 + BaseCarModel.price

    def __init__(self, model_name, year, isSunroof):
        super().__init__(model_name, year)  # Call parent constructor
        self.feature = "Sunroof" if isSunroof else "No Sunroof"

    def display_info(self):
        base_info = super().display_info()  # Call parent method
        return f"{base_info}; Feature: {self.feature}"

    def get_price(self):
        return self.deluxe_price

# Example usage:
car2 = DeluxeCarModel("Sedan LX Deluxe", 2025, isSunroof=True)
print(f"Deluxe model price is: ${car2.get_price()}")
print(f"Car info: {car2.display_info()}")
```

---

## 4. What is __init__() in Python?

**Answer:**

**Definition:**
- Constructor method (special method) automatically called when creating an object
- Initializes instance attributes and sets up the initial state

**Key Points:**
- Always the first method called when instantiating a class
- Uses `self` parameter to refer to the instance being created
- Can accept additional parameters to customize object initialization
- Not required but commonly used in most classes

**Code Example from Codebase:**

```python
# From PythonBasics/OOPS/oops.py
class Person:
    def __init__(self, name, age):
        self.name = name  # Initialize instance attributes
        self.age = age

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

# Create objects - __init__() is called automatically
person1 = Person("Raviprasad", 25)
person2 = Person("Alice", 21)

person1.display()
person2.display()
```

---

## 5. How do you read and write files in Python?

**Answer:**

**Best Practice:** Use `open()` function with context manager (`with` statement) for safe file operations.

**File Modes:**

| Mode | Description | Creates File |
|------|-------------|--------------|
| `'r'` | Read (default) | No |
| `'w'` | Write (overwrites existing) | Yes |
| `'a'` | Append | Yes |
| `'r+'` | Read and Write | No |
| `'w+'` | Write and Read (overwrites) | Yes |

**Code Example from Codebase:**

```python
# Reading files (from PythonBasics/FileOperations/read_write.py)
with open('test.txt', 'r') as f:
    content = f.read()  # Read all content
    print(f"All content of file:\n{content}\n")

# Read specific number of characters
with open('test.txt', 'r') as f:
    content_n = f.read(3)  # Read first 3 characters
    print(f"First 3 characters: {content_n}")

# Read line by line
with open('test.txt', 'r') as f:
    line1 = f.readline()
    line2 = f.readline()
    print(f"First line: {line1}")
    print(f"Second line: {line2}")

# Read all lines into a list
with open('test.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)

# Writing files
with open('output.txt', 'w') as f:
    f.write('Hello, World!')
    f.write('\nThis is a new line')

# Append to file
with open('output.txt', 'a') as f:
    f.write('\nAppended text')
```

---

## 6. What are Fixtures in Pytest? When are they used?

**Answer:**

**Definition:** Fixtures are reusable setup/teardown functions that provide test dependencies.

**Key Characteristics:**
- Defined using `@pytest.fixture` decorator
- Promote code reusability across multiple test files
- Support different scopes: `function`, `class`, `module`, `session`
- Can depend on other fixtures (fixture chaining)

**Common Use Cases:**
- Browser/WebDriver setup and teardown
- Test data initialization
- Database connections
- Authentication/login
- API client setup
- Configuration management

**Code Example from Codebase:**

```python
# From Playwright/Framework/Tests/conftest.py
import pytest
from pathlib import Path

@pytest.fixture(scope="function")
def browser_instance(playwright, request):
    browser_name = request.config.getoption("--browser_name")
    tracing_enabled = request.config.getoption("--custom-tracing") == "on"

    # Setup: Create browser and page
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    else:
        browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()

    # Start tracing if enabled
    if tracing_enabled:
        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

    yield page  # Provide page to test

    # Teardown: Stop tracing and close browser
    if tracing_enabled:
        traces_dir = Path(__file__).parent / "traces"
        traces_dir.mkdir(parents=True, exist_ok=True)
        trace_path = str(traces_dir / f"trace_{request.node.name}.zip")
        context.tracing.stop(path=trace_path)
        print(f"\nTrace saved at: {trace_path}")

    context.close()
    browser.close()
```

---

## 7. How do you use yield for WebDriver Setup and Teardown in pytest?

**Answer:**

**Purpose:** The `yield` keyword in fixtures separates setup and teardown code cleanly.

**How It Works:**
1. **Setup Code (Before yield):** Runs before the test
2. **Yield Statement:** Provides the resource to the test function
3. **Teardown Code (After yield):** Runs after the test completes

**Key Benefits:**
- Ensures proper cleanup even if test fails or raises exception
- Clean separation of concerns
- Automatic resource management
- More readable than traditional setup/teardown methods

**Code Example from Codebase:**

```python
# From Playwright/Framework/Tests/conftest.py
@pytest.fixture(scope="function")
def browser_instance(playwright, request):
    # ========== SETUP CODE ==========
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Start tracing
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )
    
    # Provide resource to test
    yield page
    
    # ========== TEARDOWN CODE ==========
    # Stop tracing and save
    traces_dir = Path(__file__).parent / "traces"
    traces_dir.mkdir(parents=True, exist_ok=True)
    trace_path = str(traces_dir / f"trace_{request.node.name}.zip")
    context.tracing.stop(path=trace_path)
    print(f"\nTrace saved at: {trace_path}")
    
    # Cleanup
    context.close()
    browser.close()

# Usage in test
def test_login(browser_instance):
    page = browser_instance
    page.goto("https://rahulshettyacademy.com/client")
    # Test code here
```

---

## 8. How do you create a list of dictionaries in Python?

**Answer:**

**Definition:** A list containing multiple dictionary objects, where each dictionary stores key-value pairs.

**Common Use Cases:**
- Test data management (credentials, test cases)
- API responses/requests
- Database query results
- Configuration settings
- User profiles

**Code Example:**

```python
# List of dictionaries - Common in test data
test_data = [
    {'username': 'user1@example.com', 'password': 'pass123', 'role': 'admin'},
    {'username': 'user2@example.com', 'password': 'pass456', 'role': 'user'},
    {'username': 'user3@example.com', 'password': 'pass789', 'role': 'guest'}
]

# Access data
for user in test_data:
    print(f"Username: {user['username']}, Role: {user['role']}")

# Access specific element
first_user = test_data[0]
print(f"First user password: {first_user['password']}")

# Filter data
admin_users = [user for user in test_data if user['role'] == 'admin']
print(f"Admin users: {admin_users}")
```

---

## 9. What is lambda function in Python?

**Answer:**

**Definition:** Anonymous, inline function defined with the `lambda` keyword.

**Characteristics:**
- Syntax: `lambda arguments: expression`
- Used for simple, one-line operations
- Cannot contain multiple statements or complex logic
- Often used with `map()`, `filter()`, `sorted()`, etc.

**When to Use:**
- Simple transformations
- Inline callbacks
- Sorting with custom keys
- Functional programming patterns

**Code Example:**

```python
# Simple lambda function
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Lambda with multiple arguments
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

# Lambda with default values
greet = lambda name="User": f"Hello, {name}!"
print(greet())  # Output: Hello, User!
print(greet("Alice"))  # Output: Hello, Alice!

# Lambda in sorting
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]
sorted_students = sorted(students, key=lambda x: x['grade'], reverse=True)
print(sorted_students)
```

---

## 10. How Lambda function applies to map() & filter() functions?

**Answer:**

**Key Concepts:**
- **`map(function, iterable)`:** Applies a function to every element in a sequence and returns a map object
- **`filter(function, iterable)`:** Filters elements based on a condition (function returns True/False)
- **Lambda Integration:** Both commonly use lambda for concise, inline function definitions

**Benefits:**
- Cleaner, more readable code
- No need to define separate functions for simple operations
- Functional programming style

**Code Example:**

```python
# MAP: Apply function to each element
numbers = [1, 2, 3, 4, 5]

# Double each number using lambda with map()
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled: {doubled}")  # Output: [2, 4, 6, 8, 10]

# Convert to squares
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared: {squared}")  # Output: [1, 4, 9, 16, 25]

# FILTER: Filter elements based on condition
# Filter numbers greater than 3
filtered = list(filter(lambda x: x > 3, numbers))
print(f"Numbers > 3: {filtered}")  # Output: [4, 5]

# Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")  # Output: [2, 4]

# Combine map and filter
result = list(map(lambda x: x * 2, filter(lambda x: x > 2, numbers)))
print(f"Even doubled (>2): {result}")  # Output: [6, 8, 10]
```

---

## 11. How do you sort a list in Python?

**Answer:**

**Two Main Methods:**

| Method | Type | Modifies Original | Returns | Use Case |
|--------|------|-------------------|---------|----------|
| `list.sort()` | In-place | Yes | None | When you want to modify the original list |
| `sorted(list)` | Returns new | No | New sorted list | When you need to keep the original |

**Common Parameters:**
- `reverse=True` - Sort in descending order
- `key=function` - Custom sorting logic (e.g., `key=lambda x: x['name']`)

**Code Example:**

```python
# In-place sorting with sort()
numbers = [5, 2, 8, 1, 9, 3]
numbers.sort()
print(f"Sorted in-place: {numbers}")  # Output: [1, 2, 3, 5, 8, 9]

# Sorting in descending order
numbers2 = [5, 2, 8, 1, 9, 3]
numbers2.sort(reverse=True)
print(f"Descending: {numbers2}")  # Output: [9, 8, 5, 3, 2, 1]

# Using sorted() - returns new list
numbers3 = [5, 2, 8, 1, 9, 3]
sorted_numbers = sorted(numbers3)
print(f"Original: {numbers3}")  # Output: [5, 2, 8, 1, 9, 3]
print(f"Sorted: {sorted_numbers}")  # Output: [1, 2, 3, 5, 8, 9]

# Sorting strings
words = ['python', 'java', 'c', 'ruby']
words.sort()
print(f"Sorted words: {words}")  # Output: ['c', 'java', 'python', 'ruby']

# Custom sorting with key parameter
students = [
    {'name': 'Alice', 'marks': 85},
    {'name': 'Bob', 'marks': 92},
    {'name': 'Charlie', 'marks': 78}
]
# Sort by marks
sorted_by_marks = sorted(students, key=lambda x: x['marks'], reverse=True)
for student in sorted_by_marks:
    print(f"{student['name']}: {student['marks']}")
```

---

## 12. Is Python asynchronous or Synchronous? What is the default type? And what is asyncio?

**Answer:**

**Python Execution Model:**
- **Default:** Synchronous - code executes line by line, blocking until each operation completes
- **Asynchronous Option:** Available via `asyncio` library using `async`/`await` keywords

**asyncio Library:**
- Enables concurrent execution of multiple tasks without multi-threading
- Best for I/O-bound operations (network requests, file operations, database queries)
- Uses event loop to manage task execution
- More efficient than threading for I/O-bound tasks

**Code Example:**

```python
import asyncio
import time

# SYNCHRONOUS (Default) - Blocks until complete
def sync_example():
    print("Start")
    time.sleep(2)  # Blocks for 2 seconds
    print("After 2 seconds")
    time.sleep(2)  # Blocks for another 2 seconds
    print("Done")  # Total time: 4 seconds

# ASYNCHRONOUS - Non-blocking
async def async_example():
    print("Start")
    await asyncio.sleep(2)  # Doesn't block, allows other tasks
    print("After 2 seconds")
    await asyncio.sleep(2)
    print("Done")  # Total time: 2 seconds (concurrent)

# Run multiple async tasks concurrently
async def run_multiple():
    await asyncio.gather(
        async_example(),
        async_example()  # Both run concurrently
    )  # Total time: 2 seconds instead of 4

# Execute synchronous
print("=== Synchronous Execution ===")
sync_example()

# Execute asynchronous
print("\n=== Asynchronous Execution ===")
asyncio.run(async_example())

print("\n=== Multiple Concurrent Tasks ===")
asyncio.run(run_multiple())
```

---

## 13. Why is the self convention used in Python? Explain with an example.

**Answer:**

**Definition:** `self` is the reference to the instance of the class, used to access instance attributes and methods.

**Key Points:**
- First parameter in instance methods
- Refers to the specific object that called the method
- Allows access to instance variables and other instance methods
- Convention (not a keyword) - technically can be named differently but strongly discouraged
- For class methods, use `cls` instead to refer to the class itself

**Code Example from Codebase:**

```python
# From PythonBasics/OOPS/oops.py
class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

# Example of self reference
class Person:
    def __init__(self, name, age):
        self.name = name  # 'self' stores data on instance
        self.age = age

    def display(self):
        # 'self' accesses instance attributes
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    def is_adult(self):
        # 'self' accesses other instance methods
        return self.age >= 18

# Creating and using objects
person1 = Person("Raviprasad", 25)
person1.display()  # self = person1
print(f"Is adult? {person1.is_adult()}")

calc = Calculator()
print(f"Addition: {calc.add(5, 3)}")  # self = calc
```

---

## 14. How do you reverse the elements of a list?

**Answer:**

**Three Main Methods:**

| Method | Type | Modifies Original | Returns | Use Case |
|--------|------|-------------------|---------|----------|
| `list.reverse()` | In-place | Yes | None | Modify existing list |
| `list[::-1]` | Slicing | No | New reversed list | Keep original intact |
| `reversed(list)` | Iterator | No | Reverse iterator | Memory-efficient iteration |

**Code Example:**

```python
# In-place reversal with reverse()
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(f"Reversed in-place: {numbers}")  # Output: [5, 4, 3, 2, 1]

# Using slice notation [::-1] - creates new list
numbers2 = [1, 2, 3, 4, 5]
reversed_list = numbers2[::-1]
print(f"Original: {numbers2}")  # Output: [1, 2, 3, 4, 5]
print(f"Reversed: {reversed_list}")  # Output: [5, 4, 3, 2, 1]

# Using reversed() function - returns iterator
numbers3 = [1, 2, 3, 4, 5]
for num in reversed(numbers3):
    print(num, end=' ')  # Output: 5 4 3 2 1
print()

# Reversing strings
text = "Hello"
reversed_text = text[::-1]
print(f"Original: {text}")  # Output: Hello
print(f"Reversed: {reversed_text}")  # Output: olleH

# Reversing list of dictionaries
students = [
    {'name': 'Alice', 'id': 1},
    {'name': 'Bob', 'id': 2},
    {'name': 'Charlie', 'id': 3}
]
students.reverse()
for student in students:
    print(student)
```

---

## 15. Explain the difference between @classmethod and instance methods.

**Answer:**

**Comparison:**

| Feature | Instance Method | Class Method | Static Method |
|---------|----------------|--------------|---------------|
| **Decorator** | None | `@classmethod` | `@staticmethod` |
| **First Parameter** | `self` (instance) | `cls` (class) | None |
| **Access Instance Data** | ✅ Yes | ❌ No | ❌ No |
| **Access Class Data** | ✅ Yes | ✅ Yes | ❌ No |
| **Common Use** | Regular operations | Factory methods | Utility functions |

**Code Example:**

```python
class Car:
    # Class variable
    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand  # Instance variable
        self.model = model  # Instance variable
        Car.total_cars += 1

    # Instance method - accesses instance data
    def display_info(self):
        return f"{self.brand} {self.model}"

    def drive(self):
        print(f"{self.brand} is driving")

    # Class method - accesses class data
    @classmethod
    def get_total_cars(cls):
        return f"Total cars created: {cls.total_cars}"

    # Class method - factory pattern
    @classmethod
    def create_from_string(cls, car_string):
        brand, model = car_string.split('-')
        return cls(brand, model)

    # Static method - doesn't access instance or class data
    @staticmethod
    def is_valid_brand(brand):
        valid_brands = ['Toyota', 'Honda', 'BMW', 'Audi']
        return brand in valid_brands

# Using instance methods
car1 = Car("Toyota", "Camry")
print(car1.display_info())  # Output: Toyota Camry
car1.drive()  # Output: Toyota is driving

# Using class method
car2 = Car("Honda", "Civic")
print(Car.get_total_cars())  # Output: Total cars created: 2

# Factory pattern with class method
car3 = Car.create_from_string("BMW-X5")
print(car3.display_info())  # Output: BMW X5

# Using static method
print(Car.is_valid_brand("Toyota"))  # Output: True
print(Car.is_valid_brand("Suzuki"))  # Output: False
```

---

## 16. What is the use of conftest.py file in Python pytest?

**Answer:**

**Definition:** Special pytest configuration file for shared fixtures and hooks.

**Key Features:**
- **Automatic Discovery:** Loaded automatically by pytest
- **Location:** Project root or test directories
- **Scope:** Fixtures available across multiple test files in the same directory and subdirectories
- **Content:** Shared fixtures, hooks, custom pytest plugins, command-line options

**Common Use Cases:**
- Define reusable fixtures (browser, database, API clients)
- Add custom command-line options
- Configure pytest hooks
- Share test data and utilities

**Code Example from Codebase:**

```python
# From Playwright/Framework/Tests/conftest.py
import pytest
from pathlib import Path

@pytest.fixture(scope="session")
def test_credentials(request):
    """Session-scoped fixture - shared across all tests"""
    return request.param

def pytest_addoption(parser):
    """Add custom command-line options"""
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser name to run tests against (chromium, firefox, webkit)",
    )
    parser.addoption(
        "--custom-tracing",
        action="store",
        default="on",
        choices=["on", "off"],
        help="Enable or disable Playwright tracing (on/off)",
    )

@pytest.fixture(scope="function")
def browser_instance(playwright, request):
    """Function-scoped fixture - creates new instance per test"""
    browser_name = request.config.getoption("--browser_name")
    tracing_enabled = request.config.getoption("--custom-tracing") == "on"

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    if tracing_enabled:
        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

    yield page

    if tracing_enabled:
        traces_dir = Path(__file__).parent / "traces"
        traces_dir.mkdir(parents=True, exist_ok=True)
        trace_path = str(traces_dir / f"trace_{request.node.name}.zip")
        context.tracing.stop(path=trace_path)

    context.close()
    browser.close()
```

---

## 17. How do you execute only failed test cases in pytest?

**Answer:**

**Command Options:**

| Command | Description | Use Case |
|---------|-------------|----------|
| `pytest --lf` or `--last-failed` | Run only tests that failed in the last run | Quick debugging |
| `pytest --ff` or `--failed-first` | Run failed tests first, then others | Priority execution |
| `pytest --lf -x` | Run failed tests and stop on first failure | Debug one at a time |

**Key Points:**
- Requires previous test run to have failure history
- Saves time during debugging cycles
- Works with cache from `.pytest_cache/` directory

**Terminal Commands:**

```bash
# Run all tests
python -m pytest

# Run only last failed tests
python -m pytest --lf

# Run failed tests first, then passed tests
python -m pytest --ff

# Run specific failed test
python -m pytest -k test_name

# Run with verbose output
python -m pytest --lf -v

# Run failed tests and stop on first failure
python -m pytest --lf -x
```

---

## 18. How do you apply a custom marker to a test case in pytest?

**Answer:**

**Definition:** Markers allow grouping and selective execution of tests based on custom tags.

**How to Use:**
1. **Apply Marker:** Use `@pytest.mark.markername` decorator on test functions
2. **Register Markers:** Add to `pytest.ini` to avoid warnings
3. **Run Tests:** Use `-m` flag to filter tests by marker

**Benefits:**
- Organize tests into logical groups (smoke, regression, slow, etc.)
- Run specific test suites
- Combine markers with boolean logic

**Code Example from Codebase:**

```python
# From Playwright/E2E/test_e2eFlowHybrid.py
import pytest

@pytest.mark.smoke
def test_createOrderAndVerify(playwright):
    """Test marked as smoke test"""
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("RahulChowdhary@gmail.com")
    # More test code...

# From Playwright/Framework/Tests/test_e2eFlowHybridFramework.py
@pytest.mark.smoke
@pytest.mark.e2e
def test_e2eFlow(page):
    """Test with multiple markers"""
    page.goto("https://example.com")
    # Test code...

# Create pytest.ini to register custom markers
"""
[pytest]
markers =
    smoke: marks tests as smoke tests
    e2e: marks tests as end-to-end tests
    regression: marks tests as regression tests
    slow: marks tests as slow running
"""
```

**Terminal Commands:**

```bash
# Run only smoke tests
python -m pytest -m smoke

# Run smoke AND e2e tests
python -m pytest -m "smoke or e2e"

# Run smoke tests but NOT e2e
python -m pytest -m "smoke and not e2e"

# Run with parallel execution using xdist
python -m pytest -n 5 --html=report.html -m smoke

# Run with tracing enabled
python -m pytest -n 5 --html=report.html --custom-tracing on
```

---

## 19. What is the Python "with" statement designed for?

**Answer:**

**Definition:** Context management protocol for automatic resource handling.

**Purpose:**
- Automatically handles setup (entering context) and cleanup (exiting context)
- Guarantees cleanup code runs even if exceptions occur
- Eliminates the need for manual resource cleanup

**Common Use Cases:**
- File operations (automatic file closing)
- Database connections
- Network sockets
- Thread locks
- Playwright browser contexts

**Code Example:**

```python
# File operations with context manager
with open('test.txt', 'r') as f:
    content = f.read()  # File is read
    print(content)
# File is automatically closed here, even if error occurred

# Writing files
with open('output.txt', 'w') as f:
    f.write('Hello, World!')
    f.write('\nSecond line')
# File automatically flushed and closed

# Multiple context managers
with open('input.txt', 'r') as f1, open('output.txt', 'w') as f2:
    for line in f1:
        f2.write(line.upper())
# Both files automatically closed

# Playwright context manager
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Use page
    page.goto("https://example.com")
    
# Browser automatically closed here

# Multiple nested contexts
with open('file.txt', 'r') as f:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        
        # Use both file and browser
        content = f.read()
        page.goto("https://example.com")
        
    # Browser closed automatically
# File closed automatically

# Custom context manager class
from contextlib import contextmanager

@contextmanager
def resource_manager(name):
    print(f"Setting up {name}")
    try:
        yield f"Resource: {name}"
    finally:
        print(f"Cleaning up {name}")

# Usage
with resource_manager("Database") as res:
    print(f"Using: {res}")
# Output:
# Setting up Database
# Using: Resource: Database
# Cleaning up Database
```

---

## 20. How to Handle Exceptions in Python? Where does the finally keyword come into play with exceptions?

**Answer:**

**Exception Handling Components:**

| Block | Purpose | When It Runs |
|-------|---------|--------------|
| `try` | Contains code that might raise exception | Always |
| `except` | Catches and handles specific exceptions | Only if exception occurs |
| `else` | Executes if no exception occurs (optional) | Only if no exception |
| `finally` | Cleanup code that always runs | Always, regardless of exception |

**Key Points:**
- Multiple `except` blocks can handle different exception types
- `raise` keyword manually raises exceptions
- `finally` ensures cleanup (close files, connections, etc.)
- Best practice: catch specific exceptions rather than generic `Exception`

**Code Example:**

```python
# Basic exception handling
try:
    result = 10 / 2  # Normal execution
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result: {result}")  # Executes if no exception
finally:
    print("Cleanup code - always runs")

# Output:
# Result: 5
# Cleanup code - always runs

# Exception with division by zero
try:
    result = 10 / 0  # Raises exception
except ZeroDivisionError:
    print("Cannot divide by zero!")  # Catches and handles
except TypeError:
    print("Type error occurred")
else:
    print(f"Result: {result}")
finally:
    print("Cleanup code - always runs")

# Output:
# Cannot divide by zero!
# Cleanup code - always runs

# Multiple specific exceptions
try:
    data = {'name': 'Alice'}
    print(data['age'])  # Raises KeyError
except KeyError as e:
    print(f"Key not found: {e}")
except ValueError as e:
    print(f"Value error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("Cleanup operations")

# Raising custom exceptions
def validate_age(age):
    try:
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age > 150:
            raise ValueError("Age seems unrealistic")
        return True
    except ValueError as e:
        print(f"Validation error: {e}")
        raise  # Re-raise the exception
    finally:
        print("Age validation attempted")

# File operations with exception handling
try:
    with open('nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
except IOError as e:
    print(f"IO Error: {e}")
finally:
    print("File operation completed")

# Real-world Playwright example
from playwright.sync_api import sync_playwright

try:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        try:
            page = browser.new_page()
            page.goto("https://example.com", timeout=5000)
        except Exception as e:
            print(f"Navigation error: {e}")
        finally:
            browser.close()  # Always close browser
except Exception as e:
    print(f"Fatal error: {e}")
finally:
    print("Test cleanup complete")
```

---

## Running Tests with Different Options

### Basic Test Execution:
```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest Playwright/part1/test_coreLocators.py

# Run specific test function
python -m pytest Playwright/part1/test_coreLocators.py::test_core_locators

# Run with verbose output
python -m pytest -v
```

### Parallel Execution:
```bash
# Run with 5 workers
python -m pytest -n 5

# Run with 5 workers and specific browser
python -m pytest -n 5 --browser_name chromium
```

### With HTML Report:
```bash
# Generate HTML report
python -m pytest --html=report.html

# Parallel execution with HTML report
python -m pytest -n 5 --html=report.html
```

### With Tracing (Playwright):
```bash
# Enable tracing (traces saved in traces folder)
python -m pytest -n 5 --html=report.html --custom-tracing on

# Disable tracing
python -m pytest -n 5 --html=report.html --custom-tracing off

# Run smoke tests with tracing
python -m pytest -m smoke -n 5 --html=report.html --custom-tracing on
```

### With Markers:
```bash
# Run only smoke tests
python -m pytest -m smoke

# Run smoke and e2e tests
python -m pytest -m "smoke or e2e"

# Run all except slow tests
python -m pytest -m "not slow"
```

---

## Trace Folder Location

When running tests with `--custom-tracing on`, traces are saved at:
```
C:\Users\916992\github\PythonPlaywright\Playwright\Framework\Tests\traces\
```

Each trace file follows the naming pattern: `trace_{test_name}.zip`

Example:
```
C:\Users\916992\github\PythonPlaywright\Playwright\Framework\Tests\traces\trace_test_e2eFlow.zip
```

---

This document provides comprehensive Q&A with practical code examples from the actual codebase!

