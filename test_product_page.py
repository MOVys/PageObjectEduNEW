from .pages.main_page import MainPage
from .pages.product_page import ProductPage
#from .base_page import BasePage
from selenium.webdriver.common.by import By
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_buy_book()
    time.sleep(5)    