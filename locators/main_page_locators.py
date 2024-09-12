"""Модуль содержит локаторы для раздела 'Главная страница' с основным функционалом"""
from selenium.webdriver.common.by import By


class MainPageLocators:
    #  КНОПКИ НА ГЛАВНОЙ СТРАНИЦЕ
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text() = "Конструктор"]')
    INGREDIENT_MODAL_CLOSE_BUTTON = (By.XPATH, '//*[@id="root"]/div/section[1]/div[1]/button')
    ORDER_BUTTON = (By.XPATH, '//button[text() = "Оформить заказ"]')
    ORDER_MODAL_CLOSE_BUTTON = (By.XPATH, '//section[contains(@class, "Modal_modal_opened__3ISw4 '
                                          'Modal_modal__P3_V5")]//button[contains(@class, "Modal_modal__close")]')

    #  ТЕКСТЫ НА ГЛАВНОЙ СТРАНИЦЕ
    CONSTRUCT_BURGER_TEXT = (By.XPATH, '//h1[text() = "Соберите бургер"]')
    INGREDIENT_MODAL_TEXT = (By.XPATH, '//h2[text() = "Детали ингредиента"]')
    ORDER_MODAL_TEXT = (By.XPATH, '//p[text() = "идентификатор заказа"]')
    ORDER_NUMBER_IN_MODAL = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')

    #  ДРУГИЕ ЭЛЕМЕНТЫ НА ГЛАВНОЙ СТРАНИЦЕ
    INGREDIENT_ELEMENT = (By.XPATH, '//p[contains(@*,"BurgerIngredient_ingredient") and text() = "Флюоресцентная '
                                    'булка R2-D3"]')
    CONSTRUCTOR_ELEMENT = (By.XPATH, '//span[1][text() = "Перетяните булочку сюда (верх)"]')
    INGREDIENT_COUNTER = (By.CLASS_NAME, 'counter_counter__num__3nue1')
