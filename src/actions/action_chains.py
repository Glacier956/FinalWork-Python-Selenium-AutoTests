from selenium import webdriver
import pytest
import allure


@pytest.fixture
def moving_mouse_to_product(selenium):
    @allure.step('Перемещение мышки на товар')
    def callback(product):
        action_chains = webdriver.ActionChains(selenium)
        action_chains.move_to_element(product).release().perform()
    return callback
