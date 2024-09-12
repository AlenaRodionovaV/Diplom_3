import allure
from conftest import driver
from pages.account_page import AccountPage
from pages.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecovery:
    @allure.title("Проверяем переход на страницу восстановления пароля по кнопке 'Восстановить пароль' на странице "
                  "авториазции")
    def test_open_password_recovery_page(self, driver):
        open_account = AccountPage(driver)
        open_account.click_on_account_button()
        open_account.wait_visibility_of_login_text()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.click_on_recovery_password_button()
        password_recovery_page.wait_visibility_of_recovery_password_text()
        assert password_recovery_page.check_recovery_password_text_is_displayed()

    @allure.title("Проверяем ввод почты и клик по кнопке 'Восстановить'")
    def test_filling_and_recovering_password(self, driver):
        open_account = AccountPage(driver)
        open_account.click_on_account_button()
        open_account.wait_visibility_of_login_text()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.click_on_recovery_password_button()
        password_recovery_page.wait_visibility_of_recovery_password_text()
        password_recovery_page.send_keys_to_email_input()
        password_recovery_page.click_on_recovery_button()
        password_recovery_page.wait_visibility_of_password_input()
        assert password_recovery_page.check_password_input_is_displayed()

    @allure.title("Проверяем, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_click_password_icon(self, driver):
        open_account = AccountPage(driver)
        open_account.click_on_account_button()
        open_account.wait_visibility_of_login_text()
        password_recovery_page = PasswordRecoveryPage(driver)
        password_recovery_page.click_on_recovery_password_button()
        password_recovery_page.wait_visibility_of_recovery_password_text()
        password_recovery_page.send_keys_to_email_input()
        password_recovery_page.click_on_recovery_button()
        password_recovery_page.wait_visibility_of_password_input()
        password_recovery_page.click_on_password_icon()
        assert password_recovery_page.check_password_input_is_active()
