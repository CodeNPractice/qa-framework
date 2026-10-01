from config import BASE_URL

class LoginPage:
    URL = BASE_URL
    
    def __init__(self, page):
        self.page = page
        
    def open(self):
        self.page.goto(self.URL)
        
    def login(self, username, password):
        self.page.fill("[data-test='username']", username)
        self.page.fill("[data-test='password']", password)
        self.page.click("[data-test='login-button']")
        
    def error_message(self):
        
        return self.page.locator("[data-test='error']")
    
    