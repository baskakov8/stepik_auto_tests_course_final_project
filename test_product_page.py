import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

base_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestUserAddToBasketFromProductPage:
    '''Description of adding product to the basket by user'''

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        self.fake_password = 'FakePassword' + str(time.time())
        self.fake_email = str(time.time()) + '@fakemail.org'
        self.browser = browser
        page = ProductPage(self.browser, base_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(self.browser, self.browser.current_url)
        login_page.register_new_user(self.fake_email, self.fake_password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        page = ProductPage(self.browser, base_link)
        page.open()
        page.should_add_product_to_basket_without_quiz()

    def test_user_cant_see_success_message(self):
        page = ProductPage(self.browser, base_link)
        page.open()
        page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.should_add_product_to_basket_without_quiz()

@pytest.mark.parametrize('link', [f'{base_link}?promo=offer{i}' if i != 7 else pytest.param(f'{base_link}?promo=offer{i}', marks=pytest.mark.xfail) for i in range(10)])
def test_guest_can_add_product_to_basket_promo(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_add_product_to_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.should_add_product_to_basket_without_quiz()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.should_add_product_to_basket_without_quiz()
    page.should_disappeared_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_products_in_basket()
    basket_page.should_be_text_basket_empty()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

if __name__ == '__main__':
    pytest.main()
