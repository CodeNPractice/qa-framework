import re
from playwright.sync_api import sync_playwright, expect

def test_now():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://python.org")
        page.fill("input[name='q']", "pytest")
        page.press("input[name='q']", "Enter")

        expect(page).to_have_url(re.compile("pytest"))
        expect(page.locator("ul.list-recent-events li").first).to_be_visible()

        browser.close()