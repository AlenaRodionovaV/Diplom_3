"""Модуль содержит методы взаимодействия с элементами на главной странице с основным функционалом"""
import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Нажимаем кнопку 'Конструктор' на главной странице")
    def click_on_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Ждем появление текста 'Соберите бургер' на главной странице")
    def wait_visibility_of_burger_text(self):
        self.wait_visibility_of_element(MainPageLocators.CONSTRUCT_BURGER_TEXT)

    @allure.step("Проверяем отображение текста 'Соберите бургер' на главной странице")
    def check_burger_text_is_displayed(self):
        return self.check_displaying_of_element(MainPageLocators.CONSTRUCT_BURGER_TEXT)

    @allure.step("Нажимаем на ингредиент на главной странице")
    def click_on_ingredient(self):
        self.click_on_element(MainPageLocators.INGREDIENT_ELEMENT)

    @allure.step("Ждем появление модального окна с текстом 'Детали ингредиента' на главной странице")
    def wait_visibility_of_ingredient_details_modal(self):
        self.wait_visibility_of_element(MainPageLocators.INGREDIENT_MODAL_TEXT)

    @allure.step("Нажимаем на крестик закрытия модального окна с деталями ингредиента")
    def click_on_ingredient_modal_close_button(self):
        self.click_on_element(MainPageLocators.INGREDIENT_MODAL_CLOSE_BUTTON)

    @allure.step("Проверяем, что модалка с деталями ингредиента закрылась")
    def check_ingredient_modal_is_not_displayed(self):
        self.wait_absence_of_element(MainPageLocators.INGREDIENT_MODAL_TEXT)
        if not self.check_displaying_of_element(MainPageLocators.INGREDIENT_MODAL_TEXT):
            return True

    @allure.step("Перетаскиваем ингредиент в конструктор")
    def drag_and_drop_ingredient_to_constructor(self):
        ingredient_element = self.find_element(MainPageLocators.INGREDIENT_ELEMENT)
        target_element = self.find_element(MainPageLocators.CONSTRUCTOR_ELEMENT)
        self.drag_and_drop_element(ingredient_element, target_element)

    @allure.step("Проверяем изменение каунтера ингредиента")
    def get_ingredient_counter_value(self):
        return self.get_text_of_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step("Нажимаем кнопку 'Оформить заказ' на глвной странице")
    def click_on_make_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step("Ждем появление модального окна с текстом 'Ваш заказ начали готовить' на главной странице")
    def wait_visibility_of_order_details_modal(self):
        self.wait_visibility_of_element(MainPageLocators.ORDER_MODAL_TEXT)

    @allure.step("Проверяем отображение модального окна с текстом 'Ваш заказ начали готовить'")
    def check_order_details_modal_is_displayed(self):
        return self.check_displaying_of_element(MainPageLocators.ORDER_MODAL_TEXT)

    @allure.step("Берём номер заказа, отображающийся в модальном окне")
    def get_order_number(self):
        self.wait_for_element_to_change_text(MainPageLocators.ORDER_NUMBER_IN_MODAL, '9999')
        return self.get_text_of_element(MainPageLocators.ORDER_NUMBER_IN_MODAL)

    @allure.step("Ждем, когда крестик закрытия модального окна можно нажимать")
    def wait_order_modal_close_button_is_clickable(self):
        return self.wait_element_to_be_clickable(MainPageLocators.ORDER_MODAL_CLOSE_BUTTON)

    @allure.step("Закрываем модальное окно с текстом 'Ваш заказ начали готовить'")
    def click_on_order_modal_close_button(self):
        return self.click_on_element(MainPageLocators.ORDER_MODAL_CLOSE_BUTTON)
