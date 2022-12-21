"""
Тесты для работы с конкретным продуктом
Start test
pytest -v --tb=line --language=en test_product_page.py

Если вам нужна дополнительная информация, использовать -v
"""
import pytest

from .pages.base_page import BasePage
from .pages.product_page import ProductPage
import time


@pytest.mark.parametrize('endpoint', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, endpoint):
    """Проверка добавления товара в корзину"""
    # link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{endpoint}"

    page = BasePage(browser, link)
    page.open()

    page_basket = ProductPage(browser, link)

    # Чек названия продукта и его цены
    page_basket.add_product_into_the_basket()  # добавить продукт в корзину
    page_basket.solve_quiz_and_get_code()  # Работа с аллертом

    # Проверка что товар добавлен в корзину
    page_basket.product_in_basket_check()

    # Проверка что стоимость корзины равна стоимости товара
    page_basket.check_value_price_basket()

    # page_basket.go_to_the_basket()
