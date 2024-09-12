import allure
from conftest import driver
from pages.account_page import AccountPage


class TestAccountPage:
    @allure.title("Проверяем переход по клику 'Личный кабинет'")
    def test_open_account(self, driver):
        open_account = AccountPage(driver)
        open_account.click_on_account_button()
        assert open_account.check_login_text_is_displayed()

    @allure.title("Проверяем переход в раздел 'История заказов'")
    def test_open_account(self, driver):
        order_history = AccountPage(driver)
        order_history.click_on_account_button()
        order_history.wait_visibility_of_login_text()
        order_history.send_keys_to_email_input_in_account()
        order_history.send_keys_to_password_input_in_account()
        order_history.click_on_login_button()
        order_history.wait_visibility_of_burger_text()
        order_history.click_on_account_button()
        order_history.wait_visibility_of_change_info_text()
        order_history.click_on_orders_history_button()
        order_history.wait_visibility_of_first_order()
        assert order_history.check_first_order_is_displayed()

    @allure.title("Проверяем выход из аккаунта")
    def test_logout(self, driver):
        logout = AccountPage(driver)
        logout.click_on_account_button()
        logout.wait_visibility_of_login_text()
        logout.send_keys_to_email_input_in_account()
        logout.send_keys_to_password_input_in_account()
        logout.click_on_login_button()
        logout.wait_visibility_of_burger_text()
        logout.click_on_account_button()
        logout.wait_visibility_of_change_info_text()
        logout.click_on_logout_button()
        logout.wait_visibility_of_login_text()
        assert logout.check_login_text_is_displayed()
