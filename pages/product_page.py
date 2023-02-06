import time

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    """Взаимодействие с продуктом"""

    def add_product_into_the_basket(self):
        """Найти кнопку добавления в корзину - Добавить в корзину"""
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_THE_BASKET)
        basket_button.click()

    def go_to_the_basket(self):
        """Перейти в корзину"""
        basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket.click()

    def product_in_basket_check(self):
        """Проверка всплывашки, что товар добавлен в корзину"""
        product_in_main_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME) #Наименование продукта в основной странице
        product_in_main_page_text = product_in_main_page.text

        product_in_inform_alert_window = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_THE_BASKET) #Наименование продукта в всплывающем окне
        product_in_inform_alert_window_text = product_in_inform_alert_window.text

        assert product_in_main_page_text == product_in_inform_alert_window_text, "Какой то левый товар был добавлен в корзину"

    def check_value_price_basket(self):
        """Проверка всплывашки"""
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_text = product_price.text

        basket_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_THE_BASKET)
        basket_price_text = basket_price.text

        assert product_price_text == basket_price_text, "Стоимость товара не равна общей стоимости корзины"


    def solve_quiz_and_get_code(self):
        """Переключиться на алерт, заполнить алерт вычисленной функцией"""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            # time.sleep(10)
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


    def should_not_be_success_message_not_present(self):
        assert self.is_element_not_present(*ProductPageLocators.PRODUCT_ADD_TO_THE_BASKET), \
            "Сообщение об успешности есть, а не должно было..."


    def should_not_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADD_TO_THE_BASKET), \
            "Сообщение об успешности до сих пор есть, а не должно было..."

