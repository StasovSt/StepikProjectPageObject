from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_the_basket(self):
        """Перейти в корзину"""
        basket = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        basket.click()


    def go_to_login_page(self):
        """Поиск кнопки \"Войти или авторизоваться\" - клик по ней"""
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()


    def base_find_element(self, method, cssSelector):
        """Проверяет элемент на его наличие в DOM"""
        try:
            self.browser.find_element(method, cssSelector)
        except NoSuchElementException:
            return False
        return True

    def base_send_keys(self, element, value):
        element.send_keys(value)


    def is_element_not_present(self, method, cssSelector, timeout=4):
        """
        Проверяет элемент на его отсутствие в DOM:
        Если элемент найден возвращает False,
        Если элемент не найден кидает TimeoutException, возвращает True
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((method, cssSelector)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, method, cssSelector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((method, cssSelector)))
        except TimeoutException:
            return False

        return True

    def is_url_corrected(self):
        """Возвращает URL страницы"""
        currentUrl = self.browser.current_url
        return currentUrl

    def open(self):
        """Открыть браузер"""
        self.browser.get(self.url)

    def should_be_login_link(self):
        """Проверка на наличие кнопки  \"Войти или авторизоваться\""""
        assert self.base_find_element(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


    def should_be_authorized_user(self):
        icon_user = self.base_find_element(*BasePageLocators.USER_ICON)
        self.browser.implicitly_wait(15)
        assert icon_user, "User icon is not presented, probably unauthorised user"








