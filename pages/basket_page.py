from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        link.click()

    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), \
            "Корзина не пуста"

    def should_be_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "Отсутствует текст с указанием пустой корзины"