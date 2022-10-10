from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BtnAddToBasketLocators

class ProductPage(BasePage):
    def click_basket_button(self):
        self.browser.find_element(*BtnAddToBasketLocators.ADD_BUTTON).click()