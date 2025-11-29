import pytest


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

