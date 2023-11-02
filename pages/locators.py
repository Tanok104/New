from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BasePageLocators():
    CARD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MAIN_BOOK_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ALERT_BOOK_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    # SHOW_THE_CARD = (By.CSS_SELECTOR, "div.alertinner>p>a.btn.btn-info")
    # NAME_OF_THE_GOOD_IN_CARD = (By.CSS_SELECTOR, ".col-sm-4>h3")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")




