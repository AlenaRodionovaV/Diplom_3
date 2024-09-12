"""Модуль содержит локаторы для раздела 'Восстановление пароля'"""
from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:

    #  КНОПКИ РАЗДЕЛА ВОССТАНОВЛЕНИЯ ПАРОЛЯ
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, '//a[@href = "/forgot-password"][text() = "Восстановить пароль"]')
    RECOVERY_BUTTON = (By.XPATH, '//button[text() = "Восстановить"]')
    PASSWORD_ICON_BUTTON = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')

    #  ТЕКСТЫ РАЗДЕЛА ВОССТАНОВЛЕНИЯ ПАРОЛЯ
    PASSWORD_RECOVERY_TEXT = (By.XPATH, '//h2[text() = "Восстановление пароля"]')

    #  ИНПУТЫ РАЗДЕЛА ВОССТАНОВЛЕНИЯ ПАРОЛЯ
    EMAIL_INPUT = (By.XPATH, '//label[text() = "Email"]/following-sibling::input')
    PASSWORD_INPUT = (By.XPATH, '//label[text() = "Пароль"]/following-sibling::input')
