from .locators import AddToBasket
from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import math

class BookStore(BasePage):
    def Button_Click(self):
        try:
           self.browser.find_element(*AddToBasket.BUTTON_BASKET_LINK).click()
        except NoSuchElementException:
            print("No")

        # return BasePage(browser=self.browser, url=self.browser.current_url)

    def Name_Order(self, loc):
        try:
            #text_order = self.browser.find_element(*AddToBasket.NAME_ORDER_LINK).text
            text_order = self.browser.find_element(*loc).text
        except NoSuchElementException:
            print("No2")
        return text_order



    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
       # return self
