Feature: E2E Test Cases for Order Transaction
    As a user, I want to perform the End-to-End test cases for order transactions to ensure taht the functionality works as expected.

    Scenario: Verify order success message on order details page after placing an order
        Given User has valiid username
        And User has valid password
        And User is on the login page
        
        When User enters valid username and password
        And User clicks on the login button
        And User is navigated to the homepage
        And User selects a product from the homepage
        And User adds the product to the cart
        And User proceeds to checkout
        And User fills in the shipping and payment details
        And User confirms the order
        
        Then User should see the order success message on the order details page