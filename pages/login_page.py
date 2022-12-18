from .base_page import BasePage
from .locators import LoginPageLocators, RegisterFormLocators
import time
import pytest
from selenium import webdriver




class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        text1=self.browser.current_url
        if text1.find("login")==-1:
            assert False, "Page login is not found"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK), "Login form is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_LINK), "Registration form is not presented"

   # @pytest.fixture(scope="function")
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*RegisterFormLocators.EMAIL_LINK)
        email_field.send_keys(email)
        password_field1 = self.browser.find_element(*RegisterFormLocators.PASSWORD_LINK)
        password_field1.send_keys(password)
        password_field2 = self.browser.find_element(*RegisterFormLocators.PASSWORD_LINK_REPEAT)
        password_field2.send_keys(password)
        self.browser.find_element(*RegisterFormLocators.REGISTRATION_BUTTON).click()



