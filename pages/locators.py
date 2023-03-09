from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #Кнопка регистрации или авторизации
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_ink")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default ")  # Кнопка Посмотреть в Корзину
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BUTTON_IS_EMPTY = (By.XPATH, '//p[contains(text(), "Your")]') #Text Корзина пуста (англ)
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items") #продукт в корзине

class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, ".form-group #id_registration-email ")  # Поле для ввода email в поле регистрации
    REGISTRATION_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")  # Поле для ввода password в поле регистрации
    REGISTRATION_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")  # Поле для ввода password повторно в поле регистрации
    ADD_TO_REGISTER = (By.CSS_SELECTOR, '[value="Register"]')  # Кнопка "Зарегистрироваться"

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1") #наименование продукта в главной странице
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color") #цена продукта в главной странице
    PRODUCT_ADD_TO_THE_BASKET = (By.CSS_SELECTOR, ".alertinner strong") #Название продукта в уведомляемом окне о добавлении в корзину
    PRICE_IN_THE_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")  # цена продукта в уведомляемом окне о добавлении в корзину
    ADD_TO_THE_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket") #Добавить в корзину
