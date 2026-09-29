from playwright.sync_api import sync_playwright, expect

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com")
        page.fill("input[data-test='username']", "standard_user")
        page.fill("input[name='password']", "secret_sauce")
        page.click("input[name='login-button']")

        expect(page.locator("[data-test='title']")).to_have_text("Products")
        # assert something that only exists after login

        browser.close()


def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com")
        page.fill("input[data-test='username']", "wrong")
        page.fill("input[data-test='password']", "wrong")
        page.click("input[data-test='login-button']")

        expect(page.locator("[data-test='error']"))

        browser.close