import allure
from conftest import driver
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title("Проверяем, что при клике на заказ отображается всплывающее окно с деталями")
    def test_order_details_modal(self, driver):
        #  нажимаем на ленту заказов
        order_details_modal = OrderPage(driver)
        order_details_modal.click_on_order_tape_button()
        order_details_modal.wait_visibility_of_order_tape_text()
        #  выбираем первый заказ в ленте и нажимаем на него
        order_details_modal.click_on_first_order_in_order_list()
        order_details_modal.wait_visibility_of_order_details_modal()
        assert order_details_modal.check_order_details_modal_is_displayed()

    @allure.title("Проверяем, что заказы пользователя из раздела 'История заказов' отображаются на странице 'Лента "
                  "заказов'")
    def test_order_in_order_section(self, driver):
        #  авторизовываем пользователя
        login_user = AccountPage(driver)
        login_user.click_on_account_button()
        login_user.wait_visibility_of_login_text()
        login_user.send_keys_to_email_input_in_account()
        login_user.send_keys_to_password_input_in_account()
        login_user.click_on_login_button()
        login_user.wait_visibility_of_burger_text()
        #  создаем новый заказ
        make_order = MainPage(driver)
        make_order.drag_and_drop_ingredient_to_constructor()
        make_order.click_on_make_order_button()
        make_order.wait_visibility_of_order_details_modal()
        make_order.get_order_number()
        make_order.wait_order_modal_close_button_is_clickable()
        make_order.click_on_order_modal_close_button()
        #  достаем номер только что созданного заказа из истории заказов
        take_order_number = AccountPage(driver)
        take_order_number.click_on_account_button()
        take_order_number.wait_visibility_of_change_info_text()
        take_order_number.click_on_orders_history_button()
        take_order_number.wait_visibility_of_first_order()
        order_section = OrderPage(driver)
        order_id = order_section.get_order_number_in_order_history()
        #  проверяем, что заказ с таким номером есть в общей ленте заказов
        order_section.click_on_order_tape_button()
        assert order_section.check_order_from_order_history_in_order_section(order_id)

    @allure.title("Проверяем, что при создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_all_orders_counter_increase(self, driver):
        #  авторизовываем пользователя
        login_user = AccountPage(driver)
        login_user.click_on_account_button()
        login_user.wait_visibility_of_login_text()
        login_user.send_keys_to_email_input_in_account()
        login_user.send_keys_to_password_input_in_account()
        login_user.click_on_login_button()
        login_user.wait_visibility_of_burger_text()
        #  нажимаем на ленту заказов, чтобы сохранить значение кол-ва заказов за всё время
        orders_counter = OrderPage(driver)
        orders_counter.click_on_order_tape_button()
        all_orders_count_before_make_order = orders_counter.get_all_orders_counter_value()
        #  создаем новый заказ
        make_order = MainPage(driver)
        make_order.click_on_constructor_button()
        make_order.drag_and_drop_ingredient_to_constructor()
        make_order.click_on_make_order_button()
        make_order.wait_visibility_of_order_details_modal()
        make_order.get_order_number()
        make_order.wait_order_modal_close_button_is_clickable()
        make_order.click_on_order_modal_close_button()
        #  проверяем, что счетсик 'Выполнено за всё время' увеличился
        order_section = OrderPage(driver)
        order_section.click_on_order_tape_button()
        all_orders_count_after_make_order = order_section.get_all_orders_counter_value()
        assert all_orders_count_after_make_order > all_orders_count_before_make_order

    @allure.title("Проверяем, что при создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_today_orders_counter_increase(self, driver):
        #  авторизовываем пользователя
        login_user = AccountPage(driver)
        login_user.click_on_account_button()
        login_user.wait_visibility_of_login_text()
        login_user.send_keys_to_email_input_in_account()
        login_user.send_keys_to_password_input_in_account()
        login_user.click_on_login_button()
        login_user.wait_visibility_of_burger_text()
        #  нажимаем на ленту заказов, чтобы сохранить значение кол-ва заказов за сегодня
        orders_counter = OrderPage(driver)
        orders_counter.click_on_order_tape_button()
        all_orders_count_before_make_order = orders_counter.get_today_orders_counter_value()
        #  создаем новый заказ
        make_order = MainPage(driver)
        make_order.click_on_constructor_button()
        make_order.drag_and_drop_ingredient_to_constructor()
        make_order.click_on_make_order_button()
        make_order.wait_visibility_of_order_details_modal()
        make_order.get_order_number()
        make_order.wait_order_modal_close_button_is_clickable()
        make_order.click_on_order_modal_close_button()
        #  проверяем, что счетсик 'Выполнено за сегодня' увеличился
        order_section = OrderPage(driver)
        order_section.click_on_order_tape_button()
        all_orders_count_after_make_order = order_section.get_today_orders_counter_value()
        assert all_orders_count_after_make_order > all_orders_count_before_make_order

    @allure.title("Проверяем, что после оформления заказа его номер появляется в разделе 'В работе'")
    def test_displaying_order_in_process(self, driver):
        #  авторизовываем пользователя
        login_user = AccountPage(driver)
        login_user.click_on_account_button()
        login_user.wait_visibility_of_login_text()
        login_user.send_keys_to_email_input_in_account()
        login_user.send_keys_to_password_input_in_account()
        login_user.click_on_login_button()
        login_user.wait_visibility_of_burger_text()
        #  создаем новый заказ
        make_order = MainPage(driver)
        make_order.click_on_constructor_button()
        make_order.drag_and_drop_ingredient_to_constructor()
        make_order.click_on_make_order_button()
        make_order.wait_visibility_of_order_details_modal()
        #  получаем номер заказа
        new_order_number = make_order.get_order_number()
        #  закрываем модалку
        make_order.wait_order_modal_close_button_is_clickable()
        make_order.click_on_order_modal_close_button()
        #  проверяем, что в раздел 'В работе' добавился только что созданный заказ
        order_section = OrderPage(driver)
        order_section.click_on_order_tape_button()
        order_section.wait_visibility_of_order_tape_text()
        assert order_section.get_order_in_process_number() == '0' + new_order_number
