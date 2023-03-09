"""
Тесты для работы с конкретным продуктом
Start test
pytest -v --tb=line --language=en test_product_page.py
pytest -v --tb=line --language=en -m need_review test_product_page.py
Если вам нужна дополнительная информация, использовать -v
"""
import pytest
import time
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """Setup-функция производит авторизацию пользователя перед тестами"""
        link = "http://selenium1py.pythonanywhere.com/ru/"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())

        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()

        page_login = LoginPage(browser, link)
        page_login.register_new_user(email, password)

        page.should_be_authorized_user()

    @pytest.mark.xfail
    def test_user_cant_see_success_message(self, browser):
        """Пользователь не видит сообщение об успешном добавлении"""
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = BasePage(browser, link)
        page.open()

        page_basket = ProductPage(browser, link)
        page_basket.should_not_be_success_message_not_present()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """Проверка добавления товара в корзину
        Пользователь видит сообщение об успешном добавлении"""
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = BasePage(browser, link)
        page.open()

        page_basket = ProductPage(browser, link)

        # Чек названия продукта и его цены
        page_basket.add_product_into_the_basket()  # добавить продукт в корзину

        # Проверка что товар добавлен в корзину
        page_basket.product_in_basket_check()

        # Проверка что стоимость корзины равна стоимости товара
        page_basket.check_value_price_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = BasePage(browser, link)
    page.open()

    page_basket = ProductPage(browser, link)
    page_basket.add_product_into_the_basket()

    page_basket.should_not_be_success_message_not_present()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = BasePage(browser, link)
    page.open()

    page_basket = ProductPage(browser, link)
    page_basket.add_product_into_the_basket()

    page_basket.should_not_be_success_message_is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_the_basket()

    page.basket_is_empty_not_products()
    page.basket_is_empty_message()

@pytest.mark.need_review
@pytest.mark.parametrize('endpoint', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, endpoint):
    """Проверка добавления товара в корзину
    Пользователь видит сообщение об успешном добавлении"""
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
