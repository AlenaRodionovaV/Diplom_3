import allure
import pytest
from selenium import webdriver
from helpers.data import Urls


@allure.step("Запустить браузер. Перейти на главную страницу Stellar Burgers. Закрыть браузер по завершении теста")
@pytest.fixture(params=['firefox', 'chrome'], scope='function')
def driver(request):
    driver = None

    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()

    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()
