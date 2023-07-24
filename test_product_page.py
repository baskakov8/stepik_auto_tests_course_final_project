import pytest
import math
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from .pages.product_page import ProductPage

base_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.should_add_product_to_basket()

@pytest.mark.parametrize('link', [f'{base_link}?promo=offer{i}' if i != 7 else pytest.param(f'{base_link}?promo=offer{i}', marks=pytest.mark.xfail) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
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
