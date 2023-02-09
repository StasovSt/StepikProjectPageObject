from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):


    def register_new_user(self, email_value, password_value):

        email = BasePage()
        password1 = BasePage()
        password2 = BasePage()
        email_element = email.base_find_element(*LoginPageLocators.REGISTRTION_EMAIL)
        email.base_send_keys(email_element, email_value)

        password1_element = password1.base_find_element(*LoginPageLocators.REGISTRTION_PASS1)
        password1.base_send_keys(password1_element, password_value)

        password2_element = password2.base_find_element(*LoginPageLocators.REGISTRTION_PASS2)
        password2.base_send_keys(password2_element, password_value)


    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Corected URL check"""
        assert self.is_url_corrected() == "http://selenium1py.pythonanywhere.com/ru/accounts/login/", "Url is not current"

    def should_be_login_form(self):
        """Проверка наличия формы авторизации"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        """Проверка наличия регистрационной формы"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"
