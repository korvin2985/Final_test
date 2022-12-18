from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .locators import MainPageLocators
from .locators import BasePageLocators, BasketFromAnyPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, loc):
        try:
            self.browser.find_element(*loc)
        except NoSuchElementException:
            return False
        return True

    def should_be_login_link(self):
        return self.is_element_present(BasePageLocators.LOGIN_LINK) #, "Login link is not presented"

    def open(self):
        self.browser.get(self.url)
        return BasePage(browser=self.browser, url=self.browser.current_url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket(self):
        self.browser.find_element(*BasketFromAnyPage.BUTTON_BASKET).click()

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"



