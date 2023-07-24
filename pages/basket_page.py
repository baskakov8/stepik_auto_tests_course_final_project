from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException

class BasketPage(BasePage):
    '''Description of the main page with test methods'''

    def should_be_no_products_in_basket(self):
        assert self.are_not_product_in_basket(*BasketPageLocators.BASKET_NOT_EMPTY), 'The basket should be empty, but there are products'

    def should_be_text_basket_empty(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_EMPTY), "There isn't text that the basket is empty"

    def are_not_product_in_basket(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return True
        return False