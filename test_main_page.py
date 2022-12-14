from .pages.main_page import MainPage
from selenium.webdriver.common.by import By
#link = "http://selenium1py.pythonanywhere.com/"

# def test_guest_can_go_to_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/"
    # browser.get(link)
    # login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    # login_link.click()
    
# def go_to_login_page(browser):      #выделили в отдельную функцию
    # login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    # login_link.click()
    
# def test_guest_can_go_to_login_page(browser): 
   # browser.get(link) 
   # go_to_login_page(browser) 
   
# def test_guest_can_go_to_login_page(browser):
    # link = "http://selenium1py.pythonanywhere.com/"
    # page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    # page.open()                      # открываем страницу
    # page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()
