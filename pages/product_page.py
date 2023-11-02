from .locators import BasePageLocators
from .base_page import BasePage


class PageObject(BasePage):
    def should_be_added_thing_in_basket(self):
        self.add_to_card()
        self.should_be_thing_in_basket()
        self.should_be_the_same_prise()

    def get_name(self):
        return_name = self.browser.find_element(*BasePageLocators.MAIN_BOOK_NAME)
        return return_name.text

    def return_prise(self):
        return_prise = self.browser.find_element(*BasePageLocators.BOOK_PRICE)
        print(return_prise.text)
        return return_prise.text

    def add_to_card(self):
        add_the_basket_button = self.browser.find_element(*BasePageLocators.CARD_BUTTON)
        add_the_basket_button.click()

    def should_be_thing_in_basket(self, book_name):
        alert_book_name = self.browser.find_element(*BasePageLocators.ALERT_BOOK_NAME)
        assert book_name == alert_book_name.text, "book name is {}, but alert book name is {}".format(book_name,
                                                                                                      alert_book_name.text)

    def should_be_the_same_prise(self, book_price):
        basket_price = self.browser.find_element(*BasePageLocators.BASKET_PRICE)
        assert basket_price.text == book_price, "basket price is {}, but book price is {}".format(basket_price.text,
                                                                                                  book_price)

    def should_not_be_successful_message(self):
        assert self.is_not_element_present(
            *BasePageLocators.SUCCESS_MESSAGE), "Success message is present, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*BasePageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"
