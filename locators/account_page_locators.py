"""Модуль содержит локаторы для раздела 'Личный кабинет'"""
from selenium.webdriver.common.by import By


class AccountLocators:
    #  КНОПКИ НА СТРАНИЦЕ ЛИЧНОГО КАБИНЕТА
    ACCOUNT_BUTTON = (By.XPATH, '//a[@href = "/account"]/p[text() = "Личный Кабинет"]')
    LOGIN_BUTTON_IN_ACCOUNT = (By.XPATH, '//button[text() = "Войти"]')
    LOGOUT_BUTTON = (By.XPATH, '//button[text() = "Выход"]')
    ORDERS_HISTOTY_BUTTON = (By.XPATH, '//a[@href = "/account/order-history"][text() = "История заказов"]')

    #  ТЕКСТЫ НА СТРАНИЦЕ ЛИЧНОГО КАБИНЕТА
    LOGIN_TEXT = (By.XPATH, '//h2[text() = "Вход"]')
    CHANGE_PERSONAL_DATA_TEXT = (By.XPATH, '//p[text() = "В этом разделе вы можете изменить свои персональные данные"]')

    #  ИНПУТЫ НА СТРАНИЦЕ ЛИЧНОГО КАБИНЕТА
    EMAIL_INPUT = (By.XPATH, '//label[text() = "Email"]/following-sibling::input')
    PASSWORD_INPUT = (By.XPATH, '//label[text() = "Пароль"]/following-sibling::input')

    #  ДРУГИЕ ЭЛЕМЕНТЫ НА СТРАНИЦЕ ЛИЧНОГО КАБИНЕТА
    FIRST_ORDER_IN_ORDER_HISTORY = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')
