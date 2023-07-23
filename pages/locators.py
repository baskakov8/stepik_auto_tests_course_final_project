from selenium.webdriver.common.by import By

class MainPageLocators:
    '''Description locators for the main page'''
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    '''Description locators for the login page'''
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

