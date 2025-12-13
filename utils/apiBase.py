from typing import Any

from playwright.sync_api import Playwright

createOrderRequestBody = {
    "orders": [
        {
            "country": "India",
            "productOrderedId": "68a961459320a140fe1ca57a"
        }
    ]
}


class APIUtils:
    @staticmethod
    def getToken(playwright: Playwright, userCredentials):
        user_name = userCredentials["username"]
        password = userCredentials["password"]
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com",
                                                             ignore_https_errors=True)
        response = api_request_context.post(url="/api/ecom/auth/login"
                                            , data={
                "userEmail": user_name,
                "userPassword": password
            })
        response_body = response.json()
        print(f"\n Login/getToken response body is: \n{response_body}")
        return response_body["token"]

    @staticmethod
    def createOrder(playwright: Playwright, userCredentials) -> Any:
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com",
                                                             ignore_https_errors=True)
        response = api_request_context.post(url="/api/ecom/order/create-order"
                                            , data=createOrderRequestBody
                                            , headers={"Authorization": APIUtils.getToken(playwright, userCredentials),
                                                       "Content-type": "application/json"})
        responseBody = response.json()
        print(f"\n Create order response body: \n{responseBody}")
        return responseBody["orders"][0]
