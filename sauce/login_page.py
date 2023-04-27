from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self) -> "LoginPage":
        self.page.goto("https://www.saucedemo.com/")
        return self

    def login(self, username: str, password: str = "secret_sauce"):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")
