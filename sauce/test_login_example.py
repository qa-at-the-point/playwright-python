from playwright.sync_api import Page, expect


def test_login_with_standard_user(page: Page):
    # 1. Go to website's Login Page
    page.goto("https://www.saucedemo.com/")

    # 2. Fill in the username and password fields
    page.locator("#user-name").type("standard_user")
    page.locator("#password").type("secret_sauce")

    # 3. Click the Login button
    page.locator("#login-button").click()

    # 4. It should redirect to the Products page
    title = page.locator(".title")
    expect(title).to_have_text("Products")
