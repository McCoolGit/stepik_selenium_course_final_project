from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_to_basket_btn.click()
        self.solve_quiz_and_get_code()

    def should_product_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
               self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text, "product name is not match"
        #print(self.browser.find_element(*ProductPageLocators.COST_IN_BASKET).text)
        #print(self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text)
        assert self.browser.find_element(*ProductPageLocators.COST_IN_BASKET).text in \
               self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text, "price is not match"

