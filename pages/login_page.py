from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):

    def register_new_user(self, email_value, password_value):
        """Работаем с окном регистрации: Принимает логин и пароль - подставляет в соответствующие поля нажимает на кнопку зарегаться"""


        email_element = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_element.send_keys(email_value)

        password1_element = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS1)
        password1_element.send_keys(password_value)

        password2_element = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS2)
        password2_element.send_keys(password_value)

        register_button_element = self.browser.find_element(*LoginPageLocators.ADD_TO_REGISTER)
        register_button_element.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Corected URL check"""
        assert self.is_url_corrected() == "http://selenium1py.pythonanywhere.com/ru/accounts/login/", "Url is not current"

    def should_be_login_form(self):
        """Проверка наличия формы авторизации"""
        assert self.base_find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        """Проверка наличия регистрационной формы"""
        assert self.base_find_element(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"
