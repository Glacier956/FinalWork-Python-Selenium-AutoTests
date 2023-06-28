import allure
from selenium.webdriver.common.by import By


@allure.feature('Тестирование бонусной программы')
class TestBonusProgram:
    @allure.title('Регистрация в бонусной программе')
    def test_registration_in_the_bonus_program(self,
                                               go_to_url,
                                               wait_text_to_be_present_in_element,
                                               find_element,
                                               selenium):
        """
        Шаги:
        1. Открыть страницу http://pizzeria.skillbox.cc/bonus
        2. В поле "Имя" ввести валидное имя пользователя
        3. В поле "Телефон" ввести валидный телефон
        4. Нажать кнопку "Оформить карту"
        5. Нажать на кнопку "OK" в алерте

        Ожидаемый результат: Активация данных прошла успешно, появился текст "Ваша карта оформлена!"
        """

        name = 'Тестировщик'
        number_phone = '89999999999'

        go_to_url("http://pizzeria.skillbox.cc/bonus")
        with allure.step('Проверка валидации для полей "Имя" и "Телефон"'):
            with allure.step('Поиск кнопки "Оформить карту"'):
                button = find_element(By.CSS_SELECTOR, '[name=bonus]')
                with allure.step('Нажатие на кнопку "Оформить карту"'):
                    button.click()
            with allure.step('Ожидание появления валидаций'):
                wait_text_to_be_present_in_element(By.CSS_SELECTOR, '[id=bonus_content]',
                                                   'Поле "Имя" обязательно для заполнения')
                wait_text_to_be_present_in_element(By.CSS_SELECTOR, '[id=bonus_content]',
                                                   'Поле "Телефон" обязательно для заполнения')
        with allure.step('Проверка валидации формата поля "Телефон"'):
            with allure.step('Поиск поля "Имя" и ввод значения'):
                name_field = find_element(By.CSS_SELECTOR, '[id=bonus_username]')
                with allure.step(f'Ввод значения "{name}"'):
                    name_field.send_keys(name)
            with allure.step('Поиск поля "Телефон" и ввод значения'):
                phone_field = find_element(By.CSS_SELECTOR, '[id=bonus_phone]')
                with allure.step('Ввод значения "8"'):
                    phone_field.send_keys('8')
            with allure.step('Поиск кнопки "Оформить карту"'):
                button = find_element(By.CSS_SELECTOR, '[name=bonus]')
                with allure.step('Нажатие на кнопку "Оформить карту"'):
                    button.click()
            with allure.step('Ожидание появления валидаций'):
                wait_text_to_be_present_in_element(By.CSS_SELECTOR, '[id=bonus_content]',
                                                   'Введен неверный формат телефона')
        with allure.step('Проверка оформления карты'):
            with allure.step('Поиск поля "Имя" и ввод значения'):
                name_field = find_element(By.CSS_SELECTOR, '[id=bonus_username]')
                with allure.step(f'Ввод значения "{name}"'):
                    name_field.send_keys(name)
            with allure.step('Поиск поля "Телефон" и ввод значения'):
                phone_field = find_element(By.CSS_SELECTOR, '[id=bonus_phone]')
                with allure.step(f'Ввод значения "{number_phone}"'):
                    phone_field.send_keys(number_phone)
            with allure.step('Поиск кнопки "Оформить карту"'):
                button = find_element(By.CSS_SELECTOR, '[name=bonus]')
                with allure.step('Нажатие на кнопку "Оформить карту"'):
                    button.click()
            with allure.step('Принятие алерта'):
                selenium.switch_to.alert.accept()
            with allure.step('Ожидание завершения оформления'):
                wait_text_to_be_present_in_element(By.XPATH, '//*[contains(@id, "bonus_main")]//h3',
                                                   'Ваша карта оформлена!')
