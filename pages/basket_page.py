from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_is_empty_message(self):
        """Проверка на наличие сообщения о пустой корзине"""
        assert self.is_element_present(*BasketPageLocators.BUTTON_IS_EMPTY), "Нет сообщения что корзина пуста"


    def basket_is_empty_not_products(self):
        """Проверка на отсутствие товаров в корзине"""
        assert self.is_element_not_present(*BasketPageLocators.PRODUCT_IN_BASKET), "В корзине есть товары"
