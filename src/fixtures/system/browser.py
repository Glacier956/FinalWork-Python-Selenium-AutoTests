import allure
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
import logging
import pytest


@pytest.fixture(scope='class')
def selenium(pytestconfig):
    options = ChromeOptions()
    logging.info('Prepare chrome browser...')
    if pytestconfig.getini("headless") == 'True':
        options.add_argument("--headless")
    with allure.step('Запуск браузера'):
        driver = Chrome(options=options)
        # Делаем браузер в полноэкранный режим
        driver.maximize_window()
    logging.info('Browser chrome has been started.')
    yield driver
    # Закрываем браузер
    with allure.step('Закрытие браузера'):
        logging.info('Close chrome browser...')
        driver.quit()
