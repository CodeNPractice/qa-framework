class LoginPage:
    URL = "https://www.saucedemo.com"
    
    def __init__(self, page):
        self.page = page
        
    def open(self):
        self.page.goto(self.URL)
        
    def login(self, username, password):
        self.page.fill("[data-test='username']", username)
        self.page.fill("[data-test='password']", password)
        self.page.click("[data-test='login-button']")
        
    def error_message(self):
        #return self.page.locator("[data-test='shopping-cart-badge']")
        return self.page.locator("[data-test='error']")
    
    
class ProductPage:
    def __init__(self, page):
        self.page = page
        
    def add_to_cart(self, item):
        self.page.click(f"[data-test='add-to-cart-{item}']")
        
    def cart_badge(self):
        return self.page.locator("[data-test='shopping-cart-badge']")