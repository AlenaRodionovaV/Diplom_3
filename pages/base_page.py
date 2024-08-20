"""Модуль содержит базовые методы взаимодействия с элементами сайта"""
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Скроллим до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step("Ждем отображение элемента")
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 35).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Находим определенный элемент")
    def find_element(self, locator):
        self.wait_visibility_of_element(locator)
        return self.driver.find_element(*locator)

    @allure.step("Проверяем наличие элемента на странице")
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step("Проверяем отсутствие элемента на странице")
    def wait_absence_of_element(self, locator):
        WebDriverWait(self.driver, 20).until_not(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Проверяем, что элемент кликабельный")
    def wait_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 500).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step("Кликаем на элемент")
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Вводим значение в поле для ввода")
    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step("Перетаскиваем элемент по странице")
    def drag_and_drop_element(self, ingredient_element, target_element):
        ActionChains(self.driver).drag_and_drop(ingredient_element, target_element).pause(3).perform()

    @allure.step("Получаем текст элемента")
    def get_text_of_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Ожидаем смену текста на элементе")
    def wait_for_element_to_change_text(self, locator, value):
        return WebDriverWait(self.driver, 10).until_not(expected_conditions.
                                                        text_to_be_present_in_element(locator, value))
