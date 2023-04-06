# Test Automation using Playwright and Python

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
