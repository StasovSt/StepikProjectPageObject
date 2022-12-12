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
        basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket.click()


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
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")



