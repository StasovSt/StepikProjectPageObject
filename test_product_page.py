"""
Тесты для работы с конкретным продуктом
Start test
pytest -v --tb=line --language=en test_product_page.py
"""

from .pages.base_page import BasePage
from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    """Проверка добавления товара в корзину"""
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = BasePage(browser, link)
    page.open()

    page_basket = ProductPage(browser, link)

    #Чек названия продукта и его цены

    page_basket.add_product_into_the_basket() #добавить продукт в корзину
    page_basket.solve_quiz_and_get_code() #Работа со всплывашкой
    time.sleep(120)

    #Проверка что товар добавлен в корзину
    page_basket.product_in_basket_check()

    #Проверка что стоимость корзины равна стоимости товара
    page_basket.check_value_price_basket()


    # page_basket.go_to_the_basket()

