import pytest
from playwright.sync_api import sync_playwright
from config import USERNAME, BASE_URL, PASSWORD

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        yield page
        
        browser.close()
        
        
@pytest.fixture
def logged_in_page(page):
    page.goto(BASE_URL)
    page.fill("[data-test='username']", USERNAME)
    page.fill("[data-test='password']", PASSWORD)
    page.click("[data-test='login-button']")
    return page