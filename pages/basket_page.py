from .base_page import BasePage
from .locators import *


class BasketPage(BasePage):
    def is_not_present_in_card(self):
        assert self.is_not_element_present(*CardPageLocators.BASKET_FORMSET), "Goods present in card, but should not be"
