from Playwright.Framework.PageObjects.dashboardPage import DashboardPage


class LoginPage:
    def __init__(self, page):
        self.page = page

    # methods
    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self, test_credentials_list):
        self.page.get_by_placeholder("email@example.com").fill(test_credentials_list["username"])
        self.page.get_by_placeholder("enter your passsword").fill(test_credentials_list["password"])
        self.page.get_by_role("button", name="Login").click()
        return DashboardPage(self.page)