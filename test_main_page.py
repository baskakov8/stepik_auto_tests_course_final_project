import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    '''The first test'''
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

if __name__ == '__main__':
    pytest.main()