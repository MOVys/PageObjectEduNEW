from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")    
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")        
    
class BtnAddToBasketLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    BOOK_NAME = (By.TAG_NAME, 'h1')
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    BASKET_BOOKNAME = (By.CSS_SELECTOR, "div.alertinner ")

#content_inner > article > div.row > div.col-sm-6.product_main > h1    


