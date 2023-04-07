# Test Automation using Playwright and Python

Playwright for Python comes as a `pytest` plugin. This repo will show examples and guides on how to use Playwright for Test Automation.

> 🔗 Visit their official docs at [playwright.dev](https://playwright.dev/python/docs/writing-tests) for more details

- [Setup](#setup)
- [Playwright in Python](#playwright-in-python)
  - [Running Tests](#running-tests)
    - [Run Tests in the Terminal](#run-tests-in-the-terminal)
    - [Run Tests in VS Code](#run-tests-in-vs-code)

## Setup

> 💡 If using Gitpod, skip to `Step 4`

1. Clone the repo
2. Use `poetry` to install packages and dependencies

    ```bash
    poetry install
    ```

3. Install required browsers

    ```bash
    poetry run playwright install
    ```

4. Run test to make sure it works

    ```bash
    poetry run pytest tests/test_example.py --headed
    ```

    > 💡 If in Gitpod, you can open `Port 6080` to see the UI tests run

5. If you have no errors, you're all set! Otherwise, submit an [Issue](https://github.com/qa-at-the-point/playwright-python/issues/new)

## Playwright in Python

As you've seen in the [Setup](#setup), Playwright uses `pytest` for writing and running tests. This is good to know because most of the ways they do things (writing tests, running tests, and settings) are through `pytest`!

> 💡🔗 pytest's docs are not as _friendly_, but it's a good resource to have: [docs.pytest.org](https://docs.pytest.org/)

### Running Tests

> 🔗 Official Documentation: [playwright.dev/python/docs/running-tests](https://playwright.dev/python/docs/running-tests)

#### Run Tests in the Terminal

The base command for running tests in the Terminal is:

```bash
pytest
```

By default, this will run all tests that it finds in the project. You have a lot of control over which tests are executed, so checkout Playwright's official docs for more examples or dive into pytest's docs for more details.

> 💡 Knowing how to run tests in the Terminal is important because this is how you will run them in CI pipelines

#### Run Tests in VS Code

However, you can run and debug tests in VS Code's UI! This is great when designing, writing, and debugging tests.

- On the left of a test function, you should see a green arrow in the gutter. This is the space to the left of the line numbers
- Clicking on the green arrow will run the test in VS Code
- But, I'd suggest right-clicking the green arrow to see different run options, including the powerful `Debug Test` option

What makes `Debug Mode` so powerful? You are able to use _breakpoints_ to pause a test and be able to see what's going on at that point in the program!

For example, let's take this code snippet from our [example test file](/tests/test_example.py):

```python
➡  1    def test_login_with_standard_user(page: Page):
   2        # 1. Go to website's Login Page
   3        page.goto("https://www.saucedemo.com/")
   4
   5        # 2. Fill in the username and password fields
   6        page.locator("#user-name").type("standard_user")
   7        page.locator("#password").type("secret_sauce")
   8
   9        # 3. Click the Login button
🔴 10       page.locator("#login-button").click()
   11
   12       # 4. It should redirect to the Products page
   13       title = page.locator(".title")
   14       expect(title).to_have_text("Products")
```

On **Line 10** I've added a `breakpoint`. You can do this by clicking into the gutter space next to the line you want to stop on. Then, right-click on the green arrow and click `Debug Test`.

- The test begins to run and then stops at the breakpoint on Line 10
- The test pauses and you see some floating controls to resume the test
- This gives you a chance to see where things are at and what the browser looks like at this point in time!
