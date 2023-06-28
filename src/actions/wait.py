import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import logging


@pytest.fixture
def wait_element(selenium):
    @allure.step('Ожидание элемента по "{by}" со значением "{value}"')
    def callback(by, value):
        logging.info(f'Ожидание элемента по "{by}" со значением "{value}"')
        return WebDriverWait(selenium, 60).until(lambda driver: driver.find_element(by, value))
    return callback


@pytest.fixture
def wait_element_to_be_clickable(selenium):
    @allure.step('Ожидание элемента для клика по {by} со значением {value}')
    def callback(by, value):
        logging.info(f'Ожидание элемента для клика по {by} со значением {value}')
        return WebDriverWait(selenium, 60).until(EC.element_to_be_clickable((by, value)))
    return callback


@pytest.fixture
def wait_presence_of_element_located(selenium):
    @allure.step('Ожидание элемента для проверки наличия элемента в DOM страницы по "{by}" со значением "{value}"')
    def callback(by, value):
        logging.info(f'Ожидание элемента для проверки наличия элемента в DOM страницы по "{by}" со значением "{value}"')
        return WebDriverWait(selenium, 60).until(EC.presence_of_element_located((by, value)))
    return callback


@pytest.fixture
def wait_visibility_of_element_located(selenium):
    @allure.step('Ожидание элемента для проверки наличия элемента в DOM страницы по "{by}" со значением "{value}"')
    def callback(by, value):
        logging.info(f'Ожидание элемента для проверки наличия элемента в DOM страницы по "{by}" со значением "{value}"')
        return WebDriverWait(selenium, 60).until(EC.visibility_of_element_located((by, value)))
    return callback


@pytest.fixture
def wait_text_to_be_present_in_element(selenium):
    @allure.step('Ожидание текста "{cost_product}" в указанном элементе по "{by}" со значением "{value}"')
    def callback(by, value, cost_product):
        logging.info(f'Ожидание текста "{cost_product}" в указанном элементе по "{by}" со значением "{value}"')
        return WebDriverWait(selenium, 60).until(EC.text_to_be_present_in_element((by, value), cost_product))
    return callback
