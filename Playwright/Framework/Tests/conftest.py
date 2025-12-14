import pytest


@pytest.fixture(scope="session")
def test_credentials(request):
    return request.param
