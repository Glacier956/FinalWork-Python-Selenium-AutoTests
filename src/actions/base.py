import pytest
import allure


@pytest.fixture
def go_to_url(selenium):
    @allure.step('Открытие страницы {url}')
    def callback(url):
        selenium.get(url)
    return callback


@pytest.fixture
def clear_data(selenium):
    @allure.step('Очистка кэша и куки')
    def callback():
        selenium.execute_cdp_cmd('Storage.clearDataForOrigin', {
            "origin": '*',
            "storageTypes": 'all',
        })
    return callback
