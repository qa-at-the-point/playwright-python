import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function")
def login_with(page: Page):
    def _login_with(username: str, password: str = "secret_sauce"):
        page.goto("https://www.saucedemo.com/")
        page.locator("#user-name").type(username)
        page.locator("#password").type(password)
        page.locator("#login-button").click()

    return _login_with


USERNAMES = [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
]


@pytest.mark.parametrize("username", USERNAMES)
def test_login_with_different_roles(page: Page, login_with, username):
    """This test function will be executed 4 times with different usernames."""
    # 1. Login with the given username
    login_with(username, "secret_sauce")

    # 2. It should redirect to the Products page
    title = page.locator(".title")
    expect(title).to_have_text("Products")
