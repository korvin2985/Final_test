from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form.well")
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form.well")

class RegisterFormLocators():
    EMAIL_LINK = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_LINK = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_LINK_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    REGISTRATION_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert.alert-success.fade.in > div")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class AddToBasket():
    BUTTON_BASKET_LINK = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    #NAME_ORDER_LINK = (By.CLASS_NAME, "col-sm-6.product_main")
    NAME_ORDER_LINK = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRICE_LINK = (By.CSS_SELECTOR,"#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    NAME_ORDER_LINK1 = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")

class BasketFromAnyPage():
    h = "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a"
    h1 = "#basket_formset > div > div"
    BUTTON_BASKET = (By.CSS_SELECTOR, h)
    BUTTON_BASKET_CONTAIN = (By.CSS_SELECTOR, h)
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")


class ItemText():
    ITEM_TEXT = (By.ID, "content_inner")