from selenium.webdriver.common.by import By

class BasePageLocators:
    '''Description of locators for the base page'''
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini [href*='basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    '''Description of locators for the main page'''
    pass

class LoginPageLocators:
    '''Description of locators for the login page'''
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTER_REPEAT_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators:
    '''Description of locators for the product page'''
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    ALERT_PRICE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")

class BasketPageLocators:
    '''Description of locators for the basket page'''
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner>p')
    BASKET_NOT_EMPTY = (By.CSS_SELECTOR, '.basket_summary')
