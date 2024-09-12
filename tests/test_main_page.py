import allure
from conftest import driver
from pages.account_page import AccountPage
from pages.main_page import MainPage


class TestMainPage:
    @allure.title("Проверяем переход по клику 'Конструктор'")
    def test_open_constructor(self, driver):
        open_constructor = MainPage(driver)
        open_constructor.click_on_constructor_button()
        open_constructor.wait_visibility_of_burger_text()
        assert open_constructor.check_burger_text_is_displayed()

    @allure.title("Проверяем, что при клике на ингредиент отображается всплывающее окно с деталями, "
                  "которое закрывается кликом по крестику")
    def test_ingredient_details_modal(self, driver):
        ingredient_details_modal = MainPage(driver)
        ingredient_details_modal.wait_visibility_of_burger_text()
        ingredient_details_modal.click_on_ingredient()
        ingredient_details_modal.wait_visibility_of_ingredient_details_modal()
        ingredient_details_modal.click_on_ingredient_modal_close_button()
        assert ingredient_details_modal.check_ingredient_modal_is_not_displayed()

    @allure.title("Проверяем увеличение каунтера ингредиента при его добавлении в заказ")
    def test_ingredient_counter_increased(self, driver):
        ingredient_counter = MainPage(driver)
        ingredient_counter.drag_and_drop_ingredient_to_constructor()
        assert ingredient_counter.get_ingredient_counter_value() == '2'

    @allure.title("Проверяем, что залогиненный пользователь может оформить заказ")
    def test_authorised_user_can_make_order(self, driver):
        login_user = AccountPage(driver)
        login_user.click_on_account_button()
        login_user.wait_visibility_of_login_text()
        login_user.send_keys_to_email_input_in_account()
        login_user.send_keys_to_password_input_in_account()
        login_user.click_on_login_button()
        login_user.wait_visibility_of_burger_text()
        make_order = MainPage(driver)
        make_order.drag_and_drop_ingredient_to_constructor()
        make_order.click_on_make_order_button()
        make_order.wait_visibility_of_order_details_modal()
        assert make_order.check_order_details_modal_is_displayed()
