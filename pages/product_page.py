from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    '''Description of the product page with test methods'''

    def should_add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()
        self.should_be_product_name()
        self.should_be_product_price()

    def should_be_product_name(self):
        assert self._locators_text(ProductPageLocators.PRODUCT_NAME) == self._locators_text(ProductPageLocators.ALERT_NAME), "The wrong book was added to the basket"

    def should_be_product_price(self):
        assert self._locators_text(ProductPageLocators.PRODUCT_PRICE) == self._locators_text(ProductPageLocators.ALERT_PRICE), "The price of the books doesn't match with price in the basket"