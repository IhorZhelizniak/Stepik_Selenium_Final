from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_USER = (By.CSS_SELECTOR, '[name="registration-email"]')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '[name="registration-password1"]')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators():
    PRODUCT_ADDED = (By.XPATH, '//div[@id="messages"]/div[1]/div/strong')
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")

    BASKET_PRICE = (By.XPATH, "//div[@id='messages']/div[3]/div/p/strong")
    ACTUAL_PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']/*[@class='price_color']")

    BUY_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


