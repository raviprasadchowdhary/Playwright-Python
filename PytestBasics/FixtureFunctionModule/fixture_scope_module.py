import pytest


@pytest.fixture(scope='module')
def sample_fixture():
    print("\nSetup: Executing before the test module")
    yield
    print("\nTeardown: Executing after the test module")

def test_example_one(sample_fixture):
    print("Execution of the test example one")
    assert True

def test_example_two(sample_fixture):
    print("Execution of the test example two")
    assert True
