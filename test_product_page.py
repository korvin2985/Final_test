<<<<<<< Updated upstream
import time
from .pages.locators import AddToBasket
from .pages.product_page import BookStore
from selenium import webdriver
import pytest
from .pages.locators import BasketFromAnyPage, ItemText, RegisterFormLocators
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


# -m pytest -s test_product_page.py

browser = webdriver.Chrome(executable_path="c:\chromedriver\chromedriver.exe")
link0="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
locName0 = AddToBasket.NAME_ORDER_LINK
locName1 = AddToBasket.NAME_ORDER_LINK1
loc1 = AddToBasket.PRICE_LINK


class TestUserAddToBasketFromProductPage(BookStore):

    def test_user_can_add_product_to_basket(browser):
        # link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

        bb = BookStore(browser, link0)
        br1 = BookStore.open(bb)
        time.sleep(2)
        # print(str(br1))
        # br2 = BookStore.Button_Click(br1)
        BookStore.Button_Click(br1)
        # BookStore.solve_quiz_and_get_code(br2)
        BookStore.solve_quiz_and_get_code(br1)
        time.sleep(1)

    def test_user_cant_see_success_message(browser):
        link = "http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/"
        product_in_basket = BookStore(browser, link)
        product_in_basket_open = BookStore.open(product_in_basket)
        #product_in_basket_open.Button_Click()
        time.sleep(2)
        assert product_in_basket_open.is_not_element_present(*BasketFromAnyPage.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_same_order_name(browser, link):
    bb = BookStore(browser, link)
    br1 = BookStore.open(bb)
    t1 = BookStore.Name_Order(br1, locName0)
    BookStore.Button_Click(br1)
   # time.sleep(2)
    BookStore.solve_quiz_and_get_code(br1)
    #br1 = BookStore.solve_quiz_and_get_code(br1)
    #time.sleep(2)
    t2 = BookStore.Name_Order(br1, locName1)
    time.sleep(1)
    assert t1==t2, 'does not match'



@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", #pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_same_price(browser,link):
    bb = BookStore(browser, link)
    br1 = BookStore.open(bb)
    t1 = BookStore.Name_Order(br1, loc1)
    BookStore.Button_Click(br1)

    # BookStore.solve_quiz_and_get_code(br2)
    BookStore.solve_quiz_and_get_code(br1)
    t2 = BookStore.Name_Order(br1, loc1)
    assert t1==t2, 'does not match'


def test_guest_can_add_product_to_basket(browser):
    #link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    bb = BookStore(browser, link0)
    br1 = BookStore.open(bb)
    time.sleep(2)
    # print(str(br1))
    # br2 = BookStore.Button_Click(br1)
    BookStore.Button_Click(br1)
    # BookStore.solve_quiz_and_get_code(br2)
    BookStore.solve_quiz_and_get_code(br1)
    time.sleep(1)



@pytest.mark.login_link_page
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BookStore(browser, link)
    page.open()
    assert page.should_be_login_link(), "no such link"


@pytest.mark.login_link_page
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BookStore(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.run
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/"
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


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/"
    product_in_basket = BookStore(browser, link)
    product_in_basket_open = BookStore.open(product_in_basket)
        #product_in_basket_open.Button_Click()
    time.sleep(2)
    assert product_in_basket_open.is_not_element_present(*BasketFromAnyPage.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

email = str(time.time()) + "@fakemail.org"
password = "u7X86GCX53ga2y"
def test_registration(browser):
    reg = LoginPage(browser, link0)
    reg.open()
    reg.go_to_login_page()
    reg.register_new_user(email, password)
    time.sleep(2)
    assert reg.is_element_present(RegisterFormLocators.REGISTRATION_MESSAGE), 'not registered'




























#def test_guest_can_add_product_to_basket_promo(browser, link2):
   # bbPr = BookStore(browser, link2)
   # try:
    #    br1 = BookStore.open(bbPr)
   # except Exception:
    #    assert False, f"Link is not valid for {link2}"


=======
import time
from .pages.locators import AddToBasket
from .pages.product_page import BookStore
from selenium import webdriver
import pytest
from .pages.locators import BasketFromAnyPage, ItemText, RegisterFormLocators
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


# -m pytest -s test_product_page.py

browser = webdriver.Chrome(executable_path="c:\chromedriver\chromedriver.exe")
link0="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
locName0 = AddToBasket.NAME_ORDER_LINK
locName1 = AddToBasket.NAME_ORDER_LINK1
loc1 = AddToBasket.PRICE_LINK


class TestUserAddToBasketFromProductPage(BookStore):

    def test_user_can_add_product_to_basket(browser):
        # link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

        bb = BookStore(browser, link0)
        br1 = BookStore.open(bb)
        time.sleep(2)
        # print(str(br1))
        # br2 = BookStore.Button_Click(br1)
        BookStore.Button_Click(br1)
        # BookStore.solve_quiz_and_get_code(br2)
        BookStore.solve_quiz_and_get_code(br1)
        time.sleep(1)

    def test_user_cant_see_success_message(browser):
        link = "http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/"
        product_in_basket = BookStore(browser, link)
        product_in_basket_open = BookStore.open(product_in_basket)
        #product_in_basket_open.Button_Click()
        time.sleep(2)
        assert product_in_basket_open.is_not_element_present(*BasketFromAnyPage.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_same_order_name(browser, link):
    bb = BookStore(browser, link)
    br1 = BookStore.open(bb)
    t1 = BookStore.Name_Order(br1, locName0)
    BookStore.Button_Click(br1)
   # time.sleep(2)
    BookStore.solve_quiz_and_get_code(br1)
    #br1 = BookStore.solve_quiz_and_get_code(br1)
    #time.sleep(2)
    t2 = BookStore.Name_Order(br1, locName1)
    time.sleep(1)
    assert t1==t2, 'does not match'



@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", #pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_same_price(browser,link):
    bb = BookStore(browser, link)
    br1 = BookStore.open(bb)
    t1 = BookStore.Name_Order(br1, loc1)
    BookStore.Button_Click(br1)

    # BookStore.solve_quiz_and_get_code(br2)
    BookStore.solve_quiz_and_get_code(br1)
    t2 = BookStore.Name_Order(br1, loc1)
    assert t1==t2, 'does not match'


def test_guest_can_add_product_to_basket(browser):
    #link="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    bb = BookStore(browser, link0)
    br1 = BookStore.open(bb)
    time.sleep(2)
    # print(str(br1))
    # br2 = BookStore.Button_Click(br1)
    BookStore.Button_Click(br1)
    # BookStore.solve_quiz_and_get_code(br2)
    BookStore.solve_quiz_and_get_code(br1)
    time.sleep(1)



@pytest.mark.login_link_page
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BookStore(browser, link)
    page.open()
    assert page.should_be_login_link(), "no such link"


@pytest.mark.login_link_page
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BookStore(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.run
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/"
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


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/"
    product_in_basket = BookStore(browser, link)
    product_in_basket_open = BookStore.open(product_in_basket)
        #product_in_basket_open.Button_Click()
    time.sleep(2)
    assert product_in_basket_open.is_not_element_present(*BasketFromAnyPage.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

email = str(time.time()) + "@fakemail.org"
password = "u7X86GCX53ga2y"
def test_registration(browser):
    reg = LoginPage(browser, link0)
    reg.open()
    reg.go_to_login_page()
    reg.register_new_user(email, password)
    time.sleep(2)
    assert reg.is_element_present(RegisterFormLocators.REGISTRATION_MESSAGE), 'not registered'




























#def test_guest_can_add_product_to_basket_promo(browser, link2):
   # bbPr = BookStore(browser, link2)
   # try:
    #    br1 = BookStore.open(bbPr)
   # except Exception:
    #    assert False, f"Link is not valid for {link2}"


>>>>>>> Stashed changes
