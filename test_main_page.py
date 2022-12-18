<<<<<<< Updated upstream
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from selenium.common.exceptions import NoSuchElementException
#from .pages.base_page import BasePage


from .pages.login_page import LoginPage
from .pages.locators import BasketFromAnyPage, ItemText

#def test_guest_can_go_to_login_page(browser):
   # link = "http://selenium1py.pythonanywhere.com/"
   # browser.get(link)
   # login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
   # login_link.click()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page1(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    # login_page = page.go_to_login_page()
    # login_page.should_be_login_page()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.run
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    # page.browser.find_element(*BasketFromAnyPage.BUTTON_BASKET).click()
    page.go_to_basket()
    time.sleep(1)

    t1 = page.is_element_present(BasketFromAnyPage.BASKET_EMPTY)
    t2 = page.is_element_present(BasketFromAnyPage.BUTTON_BASKET_CONTAIN)

    assert t1, 'to write something'
    assert not t2

    assert page.is_element_present(ItemText.ITEM_TEXT), 'text to be ..'
    #print(page.browser.find_element(*ItemText.ITEM_TEXT).text)






=======
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from selenium.common.exceptions import NoSuchElementException
#from .pages.base_page import BasePage


from .pages.login_page import LoginPage
from .pages.locators import BasketFromAnyPage, ItemText

#def test_guest_can_go_to_login_page(browser):
   # link = "http://selenium1py.pythonanywhere.com/"
   # browser.get(link)
   # login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
   # login_link.click()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page1(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    # login_page = page.go_to_login_page()
    # login_page.should_be_login_page()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.run
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    # page.browser.find_element(*BasketFromAnyPage.BUTTON_BASKET).click()
    page.go_to_basket()
    time.sleep(1)

    t1 = page.is_element_present(BasketFromAnyPage.BASKET_EMPTY)
    t2 = page.is_element_present(BasketFromAnyPage.BUTTON_BASKET_CONTAIN)

    assert t1, 'to write something'
    assert not t2

    assert page.is_element_present(ItemText.ITEM_TEXT), 'text to be ..'
    #print(page.browser.find_element(*ItemText.ITEM_TEXT).text)






>>>>>>> Stashed changes
