import time
from pages.base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.url, "Не туда логинишься, алярма"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form isn't presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form isn't presented"

    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTER_USER)
        reg_email.send_keys(email)
        reg_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        reg_password.send_keys(password)
        confirm_pass = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        confirm_pass.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        button_submit.click()
