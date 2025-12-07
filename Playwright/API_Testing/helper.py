from playwright.sync_api import Playwright


def apiRequestContext(playwright: Playwright):
    api_context =  playwright.request.new_context(base_url="https://rahulshettyacademy.com", ignore_https_errors=True)
    return api_context

def getAuthToken(playwright):
    api_context = apiRequestContext(playwright)
    response = api_context.post(url="/api/ecom/auth/login"
                                , data=getAuthTokenRequestBody)
    return response.json()["token"]

def addToCartZaraCoat3(playwright):
    response = apiRequestContext(playwright).post("/api/ecom/user/add-to-cart"
                                                  , data = addToCartRequestBodyZaraCoat3
                                                  , headers={"Authorization": getAuthToken(playwright)}
                                                  )
    return response


userEmail = "RahulKumar@gmail.com"
userPassword = "Rahul@123"

getAuthTokenRequestBody = {
    "userEmail": userEmail,
    "userPassword": userPassword
    }

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

