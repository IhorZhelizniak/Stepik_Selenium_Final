from pages.base_page import BasePage
from pages.locators import ProductPageLocators



class ProductPage(BasePage):

    def should_be_promo(self):
        self.go_to_product_page()

    def go_to_product_page(self):
        new_link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
        go_to = self.browser.get(new_link)
        #link = self.browser.current_url

        "В случае необходимости оставаться на прежней ссылке, закомментировать new_link, раскомментировать link " \
        "Выбрать переменную для return"

        return go_to


    def press_buy_button(self):
        buy_button = self.browser.find_element(*ProductPageLocators.BUY_BUTTON)
        buy_button.click()


    def product_added(self):
        added_product = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert added_product.text == product_name.text, "Разные книги"

    def price_check(self):
        actual_price_find = self.browser.find_element(*ProductPageLocators.ACTUAL_PRICE)
        basket_price_find = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        basket_price = basket_price_find.text
        actual_price = actual_price_find.text
        print("\n" + basket_price + " " + actual_price)
        assert actual_price == basket_price, "Разная стоимость"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),  \
            "Message should disappear"






