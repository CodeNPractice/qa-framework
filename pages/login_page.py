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