"""Модуль содержит локаторы для раздела 'Лента заказов'"""
from selenium.webdriver.common.by import By


class OrderPageLocators:
    # КНОПКИ РАЗДЕЛА ЛЕНТА ЗАКАЗОВ
    ORDER_SECTION_BUTTON = (By.XPATH, '//a[@href = "/feed"]')

    #  ТЕКСТЫ РАЗДЕЛА ЛЕНТА ЗАКАЗОВ
    ORDER_SECTION_TEXT = (By.XPATH, '//h1[text() = "Лента заказов"]')

    #  ДРУГИЕ ЭЛЕМЕНТЫ РАЗДЕЛА ЛЕНТА ЗАКАЗОВ
    FIRST_ORDER_IN_ORDER_SECTION = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')
    ORDER_DETAILS_MODAL = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, '
                                     '"Modal_orderBox")]')
    ALL_ORDERS_COUNTER = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    TODAY_ORDERS_COUNTER = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    ORDER_IN_PROCESS = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')

    ORDER_NUMBER_IN_ORDER_HISTORY = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]/p[contains(@class, '
                                               '"text_type_digits-default")])[last()]')
    ORDER_NUMBER_IN_ORDER_SECTION = (By.XPATH, './/*[text()="{order_id}"]')
