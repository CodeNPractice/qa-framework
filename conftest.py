import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        yield page
        
        browser.close()
        
        
@pytest.fixture
def logged_in_page(page):
    page.goto("https://www.saucedemo.com")
    page.fill("[data-test='username']", "standard_user")
    page.fill("[data-test='password']", "secret_sauce")
    page.click("[data-test='login-button']")
    return page