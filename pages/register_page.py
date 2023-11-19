from .base_page import BasePage
from .main_page import MainPage
from .locators import RegisterPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time

class RegisterPage(BasePage):
    def accept_registration_rules(self):
        accept_rules_button = self.is_clickable(*RegisterPageLocators.ACCEPT_RULES_BUTTON)
        accept_rules_button.click()

    def fill_register_form(self, login, email, password):
        register_login_form = self.is_clickable(*RegisterPageLocators.REGISTER_LOGIN_FROM)
        register_login_form.send_keys(login)
        register_password_form = self.is_clickable(*RegisterPageLocators.REGISTER_PASSWORD_FROM)
        register_password_form.send_keys(password)
        register_password_repeat_form = self.is_clickable(*RegisterPageLocators.REGISTER_PASSWORD_REPEAT_FROM)
        register_password_repeat_form.send_keys(password)
        register_email_form = self.is_clickable(*RegisterPageLocators.REGISTER_EMAIL_FORM)
        register_email_form.send_keys(email)
        send_button = self.is_clickable(*RegisterPageLocators.SEND_BUTTON)
        send_button.click()

    def register_new_user(self, login, email, password):
        self.should_be_registration_rules()
        self.accept_registration_rules()
        self.should_be_register_form()
        self.fill_register_form(login, email, password)

    def should_be_register_form(self):
        assert self.is_visible(*RegisterPageLocators.REGISTER_FORM), "Register form is not presented"

    def should_be_registration_rules(self):
        assert self.is_visible(*RegisterPageLocators.RULES_FORM), "Register form is not presented"

