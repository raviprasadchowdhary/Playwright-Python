import pytest


@pytest.fixture(scope="function")
def sample_fixture():
    print("\nSetup: Executing before the test function")
    yield
    print("\nTeardown: Executing after the test function")

def test_example_one(sample_fixture):
    print("Executing the test example one")
    assert True

def test_example_two(sample_fixture):
    print("Executing the test example two")
    assert True