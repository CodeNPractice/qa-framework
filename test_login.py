from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_valid_login(page):
    
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page.locator("[data-test='title']")).to_have_text("Products")
        # assert something that only exists after login


def test_invalid_login(page):
    

    page.goto("https://www.saucedemo.com")
    page.fill("input[data-test='username']", "wrong")
    page.fill("input[data-test='password']", "wrong")
    page.click("input[data-test='login-button']")

    expect(page.locator("[data-test='error']"))

        
def test_add_to_cart(logged_in_page):

    logged_in_page.click("[data-test='add-to-cart-sauce-labs-onesie']")
    expect(logged_in_page.locator("[data-test='shopping-cart-badge']")).to_have_text('1')
