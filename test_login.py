from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.products_page import ProductPage
from config import BASE_URL, USERNAME, PASSWORD

def test_valid_login(page):
    
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(USERNAME, PASSWORD)

    expect(page.locator("[data-test='title']")).to_have_text("Products")
    # assert something that only exists after login


def test_invalid_login(page):
    
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("Wrong", "wrong")

    expect(page.locator("[data-test='error']"))

        
def test_add_to_cart(logged_in_page):

    products= ProductPage(logged_in_page)
    products.add_to_cart('sauce-labs-onesie')
    expect(products.cart_badge()).to_have_text('1')
