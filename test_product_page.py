import pytest
import math
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from .pages.product_page import ProductPage

base_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

@pytest.mark.parametrize('link', [f'{base_link}?promo=offer{i}' if i != 7 else pytest.param(f'{base_link}?promo=offer{i}', marks=pytest.mark.xfail) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_add_product_to_basket()