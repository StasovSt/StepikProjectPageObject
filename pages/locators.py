from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1") #наименование продукта в главной странице
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color") #цена продукта в главной странице

    PRODUCT_ADD_TO_THE_BASKET = (By.CSS_SELECTOR, ".alertinner strong") #Название продукта в уведомляемом окне о добавлении в корзину
    PRICE_IN_THE_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")  # Название продукта в уведомляемом окне о добавлении в корзину

    ADD_TO_THE_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")

    BASKET_BUTTON = (By.LINK_TEXT, "Посмотреть корзину")
