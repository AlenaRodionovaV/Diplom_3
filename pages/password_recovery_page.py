"""Модуль содержит методы взаимодействия с элементами в разделе восстановления пароля"""
import allure
from helpers.data import Data
from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):
    @allure.step("Нажимаем кнопку 'Восстановить пароль' на странице авторизации")
    def click_on_recovery_password_button(self):
        self.click_on_element(PasswordRecoveryLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step("Ждем появление текста 'Восстановление пароля' на странице восстановления пароля")
    def wait_visibility_of_recovery_password_text(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.PASSWORD_RECOVERY_TEXT)

    @allure.step("Проверяем появление текста 'Восстановление пароля' на странице восстановления пароля")
    def check_recovery_password_text_is_displayed(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.PASSWORD_RECOVERY_TEXT)

    @allure.step("Заполняем поле 'Email' на странице восстановления пароля")
    def send_keys_to_email_input(self):
        self.send_keys_to_input(PasswordRecoveryLocators.EMAIL_INPUT, Data.EMAIL)

    @allure.step("Нажимаем на кнопку 'Восстановить' на странице восстановления пароля")
    def click_on_recovery_button(self):
        self.click_on_element(PasswordRecoveryLocators.RECOVERY_BUTTON)

    @allure.step("Ждем появление поля 'Пароль'")
    def wait_visibility_of_password_input(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.PASSWORD_INPUT)

    @allure.step("Проверяем появление поля 'Пароль' на странице восстановления пароля")
    def check_password_input_is_displayed(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.PASSWORD_INPUT)

    @allure.step("Нажимаем иконку скрытия/показа пароля")
    def click_on_password_icon(self):
        self.click_on_element(PasswordRecoveryLocators.PASSWORD_ICON_BUTTON)

    @allure.step("Ожидаем, что поле 'Пароль' подсвечивается и становится активным")
    def check_password_input_is_active(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.PASSWORD_INPUT)
