"""Start test
pytest -v --tb=line --language=en test_main_page.py
"""

import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page_login = LoginPage(browser, link)
    page_login.open()
    page_login.should_be_login_form()

def test_guest_can_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

    page_login = LoginPage(browser, browser.current_url)
    page_login.should_be_register_form()

@pytest.mark.skip
def test_login_url_is_corrected(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page_login = LoginPage(browser, link)
    page_login.open()
    page_login.should_be_login_url()