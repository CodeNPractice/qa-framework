class ProductPage:
    def __init__(self, page):
        self.page = page
        
    def add_to_cart(self, item):
        self.page.click(f"[data-test='add-to-cart-{item}']")
        
    def cart_badge(self):
        return self.page.locator("[data-test='shopping-cart-badge']")