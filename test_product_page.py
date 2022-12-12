"""
Тесты для работы с конкретным продуктом
Start test
pytest -v --tb=line --language=en test_product_page.py
"""

from .pages.base_page import BasePage
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    """Проверка добавления товара в корзину"""
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = BasePage(browser, link)
    page.open()

    page_basket = ProductPage(browser, link)
    page_basket.add_product_into_the_basket()
    page_basket.solve_quiz_and_get_code()

    # page_basket.go_to_the_basket()
    # time.sleep(5)
