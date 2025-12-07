from Playwright.API_Testing.helper import *


def test_getAuthToken(playwright):
    print(f"\nexecution of getAuthToken is started...")
    authToken = getAuthToken(playwright)
    print(f"Authentication token is: {authToken}")

    assert authToken is not None

def test_addToCart(playwright):
    print(f"\nexecution of addToCart is started...")
    response = addToCartZaraCoat3(playwright)
    print(f"Status code is: {response.status}")
    print(f"\nResponse body is: \n{response.json()}")

    assert response.status == 200
    assert response.json()["message"] == "Product Added To Cart"

def test_createOrder(playwright):
    print(f"\nexecution of createOrder is started...")
    response = createOrder(playwright)
    print(f"\nStatus code is: {response.status}")
    print(f"\nResponse body is: \n{response.json()}")

    assert response.status == 201
    assert response.json()["message"] == "Order Placed Successfully"
