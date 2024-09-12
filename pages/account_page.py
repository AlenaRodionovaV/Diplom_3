"""Модуль содержит методы взаимодействия с элементами в разделе личного кабинета"""
import allure
from helpers.data import Data
from locators.account_page_locators import AccountLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):

    @allure.step("Нажимаем кнопку 'Личный кабинет' на главной странице")
    def click_on_account_button(self):
        self.click_on_element(AccountLocators.ACCOUNT_BUTTON)

    @allure.step("Ждем появление текста 'Вход' на странице личного кабинета")
    def wait_visibility_of_login_text(self):
        self.wait_visibility_of_element(AccountLocators.LOGIN_TEXT)

    @allure.step("Проверяем отображение текста 'Вход' на странице личного кабинета")
    def check_login_text_is_displayed(self):
        return self.check_displaying_of_element(AccountLocators.LOGIN_TEXT)

    @allure.step("Заполняем поле 'Email' на странице личного кабинета")
    def send_keys_to_email_input_in_account(self):
        self.send_keys_to_input(AccountLocators.EMAIL_INPUT, Data.EMAIL)

    @allure.step("Заполняем поле 'Пароль' на странице личного кабинета")
    def send_keys_to_password_input_in_account(self):
        self.send_keys_to_input(AccountLocators.PASSWORD_INPUT, Data.PASSWORD)

    @allure.step("Нажимаем кнопку 'Войти' на странице личного кабинета")
    def click_on_login_button(self):
        self.click_on_element(AccountLocators.LOGIN_BUTTON_IN_ACCOUNT)

    @allure.step("Ждем появление текста 'Соберите бургер' на главной странице")
    def wait_visibility_of_burger_text(self):
        self.wait_visibility_of_element(MainPageLocators.CONSTRUCT_BURGER_TEXT)

    @allure.step("Ждем появление текста 'В этом разделе вы можете ...' в личном кабинете")
    def wait_visibility_of_change_info_text(self):
        self.wait_visibility_of_element(AccountLocators.CHANGE_PERSONAL_DATA_TEXT)

    @allure.step("Нажимаем кнопку 'История заказов' в личном кабинете")
    def click_on_orders_history_button(self):
        self.click_on_element(AccountLocators.ORDERS_HISTOTY_BUTTON)

    @allure.step("Ждем появление первого заказа в истории заказов")
    def wait_visibility_of_first_order(self):
        self.wait_visibility_of_element(AccountLocators.FIRST_ORDER_IN_ORDER_HISTORY)

    @allure.step("Проверяем отображение первого заказа в истории заказов")
    def check_first_order_is_displayed(self):
        return self.check_displaying_of_element(AccountLocators.FIRST_ORDER_IN_ORDER_HISTORY)

    @allure.step("Нажимаем кнопку 'Выход' в личном кабинете")
    def click_on_logout_button(self):
        self.click_on_element(AccountLocators.LOGOUT_BUTTON)
