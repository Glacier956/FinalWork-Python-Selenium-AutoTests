import allure
import pytest
import logging


@pytest.fixture
def find_element(selenium):
    @allure.step('Поиск элемента по "{by}" со значением "{value}"')
    def callback(by, value):
        logging.info(f'Поиск элемента по "{by}" со значением "{value}"')
        return selenium.find_element(by, value)
    return callback


@pytest.fixture
def find_elements(selenium):
    @allure.step('Поиск элементов по "{by}" со значением "{value}"')
    def callback(by, value):
        logging.info(f'Поиск элементов по "{by} со значением {value}"')
        return selenium.find_elements(by, value)
    return callback
