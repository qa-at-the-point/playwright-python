import pytest
from playwright.sync_api import Page, expect

from sauce.login_page import LoginPage


@pytest.fixture(scope="function")
def login_page(page: Page):
    return LoginPage(page).goto()


USERNAMES = [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
]


@pytest.mark.parametrize("username", USERNAMES)
def test_login_with_different_roles(page: Page, login_page, username):
    """This test function will be executed 4 times -- once for each username."""
    login_page.login(username, "secret_sauce")
    title = page.locator(".title")
    expect(title).to_have_text("Products")
