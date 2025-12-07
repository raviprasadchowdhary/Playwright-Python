from Playwright.API_Testing.helper import getAuthToken, addToCartZaraCoat3


def test_getAuthToken(playwright):
    print(f"Authentication token is: {getAuthToken(playwright)}")

    assert getAuthToken(playwright) is not None

def test_addToCart(playwright):
    print(f"\nexecution of addToCart is started...")
    print(f"Status code is: {addToCartZaraCoat3(playwright).status}")
    print(f"\nResponse body is: \n{addToCartZaraCoat3(playwright).json()}")

    assert addToCartZaraCoat3(playwright).status == 200
    assert addToCartZaraCoat3(playwright).json()["message"] == "Product Added To Cart"

