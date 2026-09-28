from selenium.webdriver.common.by import By
from pages.base_page import Base_Page


class LoginPage(Base_Page):
    
    # locators
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_btn = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")

    # actions
    def enter_username(self, username):
        self.type_text(self.username, username)
        # self.username is ('id', "user-name")
        # username is "standard_user"

    def enter_password(self, password):
        self.type_text(self.password, password)

    def click_login(self, login_btn):
        self.click(login_btn)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login(self.login_btn)

    def get_error_msg(self):
        return self.get_text(self.error_message)



