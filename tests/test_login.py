
from pages.login_page import LoginPage
from config.config import INVENTORY_URL

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert driver.current_url == INVENTORY_URL

def test_invalid_login_with_lockedout_user(driver):
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")
    assert login_page.get_error_msg() == "Epic sadface: Sorry, this user has been locked out."

def test_invalid_login_with_wrong_pwd(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "wrong_password")
    assert login_page.get_error_msg() == "Epic sadface: Username and password do not match any user in this service"

def test_invalid_login_username_blank(driver):
    login_page = LoginPage(driver)
    login_page.login("","secret_sauce")
    assert login_page.get_error_msg() == "Epic sadface: Username is required"

def test_invalid_login_pwd_blank(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "")
    assert login_page.get_error_msg() == "Epic sadface: Password is required"
