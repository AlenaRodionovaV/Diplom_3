"""Модуль содержит методы взаимодействия с элементами в разделе личного кабинета"""
import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Нажимаем кнопку 'Лента заказов' на главной странице")
    def click_on_order_tape_button(self):
        self.click_on_element(OrderPageLocators.ORDER_SECTION_BUTTON)

    @allure.step("Ждем появление текста 'Лента заказов' на странице заказов")
    def wait_visibility_of_order_tape_text(self):
        self.wait_visibility_of_element(OrderPageLocators.ORDER_SECTION_TEXT)

    @allure.step("Нажимаем на первый заказ на странице заказов")
    def click_on_first_order_in_order_list(self):
        self.click_on_element(OrderPageLocators.FIRST_ORDER_IN_ORDER_SECTION)

    @allure.step("Ждем появление модального окна с деталями заказа")
    def wait_visibility_of_order_details_modal(self):
        self.wait_visibility_of_element(OrderPageLocators.ORDER_DETAILS_MODAL)

    @allure.step("Проверяем отображение модального окна с деталями заказа")
    def check_order_details_modal_is_displayed(self):
        return self.check_displaying_of_element(OrderPageLocators.ORDER_DETAILS_MODAL)

    @allure.step("Проверяем номер заказа в карточке заказа в разделе 'История заказов'")
    def get_order_number_in_order_history(self):
        return self.get_text_of_element(OrderPageLocators.ORDER_NUMBER_IN_ORDER_HISTORY)

    @allure.step("Проверяем, что номер заказа из 'Истории заказов' отображается в 'Ленте заказов'")
    def check_order_from_order_history_in_order_section(self, order_id):
        locator = OrderPageLocators.ORDER_NUMBER_IN_ORDER_SECTION
        order_id_locator = (locator[0], locator[1].format(order_id = order_id))
        self.find_element(order_id_locator)
        return self.check_displaying_of_element(order_id_locator)

    @allure.step("Проверяем изменение каунтера заказов за всё время")
    def get_all_orders_counter_value(self):
        self.find_element(OrderPageLocators.ALL_ORDERS_COUNTER)
        return self.get_text_of_element(OrderPageLocators.ALL_ORDERS_COUNTER)

    @allure.step("Проверяем изменение каунтера заказов за сегодня")
    def get_today_orders_counter_value(self):
        self.find_element(OrderPageLocators.TODAY_ORDERS_COUNTER)
        return self.get_text_of_element(OrderPageLocators.TODAY_ORDERS_COUNTER)

    @allure.step("Берём номер заказа, отображающийся в разделе 'В работе'")
    def get_order_in_process_number(self):
        self.wait_for_element_to_change_text(OrderPageLocators.ORDER_IN_PROCESS, 'Все текущие заказы готовы!')
        return self.get_text_of_element(OrderPageLocators.ORDER_IN_PROCESS)
