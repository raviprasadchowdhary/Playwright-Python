from playwright.sync_api import Playwright


# *************************************************Functions************************************************************
# here we are creating a reusable API request context
def apiRequestContext(playwright: Playwright):
    return playwright.request.new_context(base_url="https://rahulshettyacademy.com", ignore_https_errors=True)


# here we are creating a reusable function to get the auth token
def getAuthToken(playwright):
    api_context = apiRequestContext(playwright)
    response = api_context.post(url="/api/ecom/auth/login"
                                , data=getAuthTokenRequestBody)
    return response.json()["token"]


# here we are creating a reusable function to add Zara Coat 3 to cart
def addToCartZaraCoat3(playwright):
    return apiRequestContext(playwright).post("/api/ecom/user/add-to-cart"
                                              , data=addToCartRequestBodyZaraCoat3
                                              , headers={"Authorization": getAuthToken(playwright)}
                                              )


# here we are creating a reusable function to create order for Zara Coat 3
def createOrder(playwright):
    return apiRequestContext(playwright).post(url="/api/ecom/order/create-order"
                                              , headers={"Authorization": getAuthToken(playwright)}
                                              , data=createOrderRequestBodyZaraCoat3)


# *************************************************Variables************************************************************
userEmail = "RahulKumar@gmail.com"
userPassword = "Rahul@123"

# ************************************************Request Body*********************************************************
# here we are creating reusable request body for getting auth token
getAuthTokenRequestBody = {
    "userEmail": userEmail,
    "userPassword": userPassword
}

# here we are creating reusable request body for adding Zara Coat 3 to cart
addToCartRequestBodyZaraCoat3 = {
    "_id": "693401c232ed865871222818",
    "product": {
        "_id": "68a961459320a140fe1ca57a",
        "productName": "ZARA COAT 3",
        "productCategory": "electronics",
        "productSubCategory": "mobiles",
        "productPrice": 11500,
        "productDescription": "Apple phone",
        "productImage": "https://rahulshettyacademy.com/api/ecom/uploads/productImage_1650649434146.jpeg",
        "productRating": "0",
        "productTotalOrders": "0",
        "productStatus": "true",
        "productFor": "women",
        "productAddedBy": "admin",
        "__v": 0
    }
}

# here we are creating reusable request body for creating order for Zara Coat 3
createOrderRequestBodyZaraCoat3 = {
    "orders": [
        {
            "country": "India",
            "productOrderedId": "68a961459320a140fe1ca57a"
        }
    ]
}
