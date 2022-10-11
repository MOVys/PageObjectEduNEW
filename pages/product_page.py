from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BtnAddToBasketLocators

class ProductPage(BasePage):
    def should_be_buy_book(self):
        self.add_to_basket()
        self.should_price_check()
        self.should_name_check()
        
    def add_to_basket(self):
        self.browser.find_element(*BtnAddToBasketLocators.ADD_BUTTON).click()
        self.solve_quiz_and_get_code()
        
    
    def should_price_check(self):
        product_price_check = self.browser.find_element(*BtnAddToBasketLocators.BOOK_PRICE)
        basket_price_check = self.browser.find_element(*BtnAddToBasketLocators.BASKET_PRICE)
        assert basket_price_check.text == product_price_check.text,"Цены не совпадают"

    def should_name_check(self):
        book_name = self.browser.find_element(*BtnAddToBasketLocators.BOOK_NAME)
        basket_name = self.browser.find_element(*BtnAddToBasketLocators.BASKET_BOOKNAME)
        print(basket_name, book_name)
        assert book_name.text in basket_name.text, "Названия книг не совпадают"