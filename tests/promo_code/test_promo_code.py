import datetime
import allure
from selenium.webdriver.common.by import By
import time


@allure.feature('Тестирование промокодов')
class TestPromoCode:
    @allure.title('Применение валидного промокода')
    def test_valid_promo_code(self,
                              go_to_url,
                              clear_data,
                              moving_mouse_to_product,
                              wait_text_to_be_present_in_element,
                              wait_element_to_be_clickable,
                              find_element,
                              selenium):
        """
        Шаги:
        1. Открыть страницу http://pizzeria.skillbox.cc
        2. Заполнить корзину любыми товарами
        3. Перейти в окно оформления товаров
        4. Применить промокод "GIVEMEHALYAVA"

        Ожидаемый результат: Сумма заказа уменьшилась на 10%
        """

        promo_code = 'GIVEMEHALYAVA'

        clear_data()
        go_to_url("http://pizzeria.skillbox.cc")
        with allure.step('Ожидание загрузки всех товаров в слайдере'):
            product = wait_element_to_be_clickable(By.XPATH, '//li[contains(@class, "slick-active")]'
                                                             '[contains(@data-slick-index, "3")]')
        moving_mouse_to_product(product)
        with allure.step('Поиск кнопки "В корзину"'):
            button = find_element(By.XPATH, '//li[contains(@class, "slick-active")]'
                                            '[contains(@data-slick-index, "3")]'
                                            '//a[contains(@class, "add_to_cart_button")]')
            with allure.step('Нажатие на кнопку "В корзину"'):
                button.click()
        with allure.step('Ожидание появления кнопки "Подробнее"'):
            more = wait_element_to_be_clickable(By.XPATH, '//li[contains(@class, "slick-active")]'
                                                          '[contains(@data-slick-index, "3")]'
                                                          '//a[contains(@class, "added_to_cart")]')
            with allure.step('Нажатие на кнопку "Подробнее" для перехода в корзину'):
                more.click()
        with allure.step('Поиск поля "Введите код купона" и ввод значения'):
            promo_code_field = find_element(By.CSS_SELECTOR, '[name=coupon_code]')
            with allure.step(f'Ввод значения "{promo_code}"'):
                promo_code_field.send_keys(promo_code)
        with allure.step('Поиск кнопки "Применить купон"'):
            promo_code_button = find_element(By.CSS_SELECTOR, '[name=apply_coupon]')
            with allure.step('Нажатие на кнопку "Применить купон"'):
                promo_code_button.click()
                time.sleep(2)
        with allure.step('Проверка применения купона'):
            total_cost = float(find_element(By.XPATH, '//*[contains(@class, "cart-subtotal")]'
                                                      '//span[contains(@class, "amount")]').text[:-1].replace(',', '.'))
            with allure.step(f'Получение общей стоимости заказа {total_cost}'):
                amount = total_cost * (1 - 10 / 100)
                amount = str(amount).replace('.', ',')
            with allure.step(f'Сумма заказа уменьшилась на 10% и составила "{amount}"'):
                wait_text_to_be_present_in_element(By.XPATH, '//*[contains(@class, "order-total")]'
                                                             '//span[contains(@class, "amount")]', amount)

    @allure.title('Применение не валидного промокода')
    def test_non_valid_promo_code(self,
                                  go_to_url,
                                  clear_data,
                                  moving_mouse_to_product,
                                  wait_text_to_be_present_in_element,
                                  wait_element_to_be_clickable,
                                  find_element,
                                  selenium):
        """
        Шаги:
        1. Открыть страницу http://pizzeria.skillbox.cc
        2. Заполнить корзину любыми товарами
        3. Перейти в окно оформления товаров
        4. Применить промокод "DC120"

        Ожидаемый результат: Сумма заказа не уменьшилась на 10%
        """

        promo_code = 'DC120'

        clear_data()
        go_to_url("http://pizzeria.skillbox.cc")
        with allure.step('Добавление товара в корзину и переход в нее'):
            with allure.step('Ожидание загрузки всех товаров в слайдере'):
                product = wait_element_to_be_clickable(By.XPATH, '//li[contains(@class, "slick-active")]'
                                                                 '[contains(@data-slick-index, "3")]')
            moving_mouse_to_product(product)
            with allure.step('Поиск кнопки "В корзину"'):
                button = find_element(By.XPATH, '//li[contains(@class, "slick-active")]'
                                                '[contains(@data-slick-index, "3")]'
                                                '//a[contains(@class, "add_to_cart_button")]')
                with allure.step('Нажатие на кнопку "В корзину"'):
                    button.click()
            with allure.step('Ожидание появления кнопки "Подробнее"'):
                more = wait_element_to_be_clickable(By.XPATH, '//li[contains(@class, "slick-active")]'
                                                              '[contains(@data-slick-index, "3")]'
                                                              '//a[contains(@class, "added_to_cart")]')
                with allure.step('Нажатие на кнопку "Подробнее" для перехода в корзину'):
                    more.click()
        with allure.step('Применение промокода'):
            with allure.step('Поиск поля "Введите код купона" и ввод значения'):
                promo_code_field = find_element(By.CSS_SELECTOR, '[name=coupon_code]')
                with allure.step(f'Ввод значения "{promo_code}"'):
                    promo_code_field.send_keys(promo_code)
            with allure.step('Поиск кнопки "Применить купон"'):
                promo_code_button = find_element(By.CSS_SELECTOR, '[name=apply_coupon]')
                with allure.step('Нажатие на кнопку "Применить купон"'):
                    promo_code_button.click()
                    time.sleep(2)
        with allure.step('Проверка применения промокода'):
            with allure.step('Проверка алерта, что купон неверный'):
                wait_text_to_be_present_in_element(By.CSS_SELECTOR, '[role=alert]', 'Неверный купон.')
            with allure.step('Проверка суммы заказа'):
                with allure.step('Получение общей стоимости заказа'):
                    total_cost = find_element(By.XPATH, '//*[contains(@class, "cart-subtotal")]'
                                                        '//span[contains(@class, "amount")]').text
                with allure.step('Получение суммы заказа'):
                    amount = find_element(By.XPATH, '//*[contains(@class, "order-total")]'
                                                    '//span[contains(@class, "amount")]').text
                with allure.step(f'Сравнение общей стоимости "{total_cost}" и суммы заказа "{amount}"'):
                    if total_cost != amount:
                        raise ValueError(f'Сумма заказа "{amount}" отличается от общей стоимости "{total_cost}"')

    @allure.title('Применение промокода если сервер не возвращает ответ')
    def test_errors_when_applying_a_promo_code(self,
                                               go_to_url,
                                               clear_data,
                                               moving_mouse_to_product,
                                               wait_presence_of_element_located,
                                               wait_text_to_be_present_in_element,
                                               wait_element_to_be_clickable,
                                               find_element,
                                               selenium):
        """
        Шаги:
        1. Открыть страницу http://pizzeria.skillbox.cc
        2. Заполнить корзину любыми товарами
        3. Перейти в окно оформления товаров
        4. Применить промокод "GIVEMEHALYAVA"
        5. Перехватить запрос, уходящий с веба на сервер, и заблокировать его. Не
        возвращать ответ или вернуть с ошибкой (500, например)

        Ожидаемый результат: Конечная сумма заказа НЕ уменьшилась на 10% и промокод не применился
        """

        promo_code = 'GIVEMEHALYAVA'

        clear_data()
        go_to_url("http://pizzeria.skillbox.cc")
        with allure.step('Добавление товара в корзину и переход в нее'):
            with allure.step('Ожидание загрузки всех товаров в слайдере'):
                product = wait_element_to_be_clickable(By.XPATH, '//li[contains(@class, "slick-active")]'
                                                                 '[contains(@data-slick-index, "3")]')
            moving_mouse_to_product(product)
            with allure.step('Поиск кнопки "В корзину" и клик по ней'):
                find_element(By.XPATH, '//li[contains(@class, "slick-active")]'
                                       '[contains(@data-slick-index, "3")]'
                                       '//a[contains(@class, "add_to_cart_button")]').click()
            with allure.step('Ожидание появления кнопки "Подробнее" и клик по ней'):
                wait_element_to_be_clickable(By.XPATH, '//li[contains(@class, "slick-active")]'
                                                       '[contains(@data-slick-index, "3")]'
                                                       '//a[contains(@class, "added_to_cart")]').click()
        with allure.step('Применение промокода'):
            with allure.step('Поиск поля "Введите код купона" и ввод значения'):
                promo_code_field = find_element(By.CSS_SELECTOR, '[name=coupon_code]')
                with allure.step(f'Ввод значения "{promo_code}"'):
                    promo_code_field.send_keys(promo_code)
            with allure.step('Поиск кнопки "Применить купон"'):
                promo_code_button = find_element(By.CSS_SELECTOR, '[name=apply_coupon]')
                with allure.step('Блокировка всех запросов'):
                    selenium.execute_cdp_cmd('Network.setBlockedURLs', {"urls": ["*"]})
                with allure.step('Нажатие на кнопку "Применить купон"'):
                    promo_code_button.click()
                    time.sleep(2)
        with allure.step('Проверка применения промокода'):
            with allure.step('Получение общей стоимости заказа'):
                total_cost = find_element(By.XPATH, '//*[contains(@class, "cart-subtotal")]'
                                                    '//span[contains(@class, "amount")]').text
            with allure.step('Получение суммы заказа'):
                amount = find_element(By.XPATH, '//*[contains(@class, "order-total")]'
                                                '//span[contains(@class, "amount")]').text
            with allure.step(f'Сравнение общей стоимости "{total_cost}" и суммы заказа "{amount}"'):
                if total_cost != amount:
                    raise ValueError(f'Сумма заказа "{amount}" отличается от общей стоимости "{total_cost}"')

    @allure.title('Применение промокода повторно')
    def test_reuse_promo_code(self,
                              go_to_url,
                              clear_data,
                              moving_mouse_to_product,
                              wait_text_to_be_present_in_element,
                              wait_element_to_be_clickable,
                              wait_presence_of_element_located,
                              wait_visibility_of_element_located,
                              find_element,
                              selenium):
        """
        Шаги:
        1. Открыть страницу http://pizzeria.skillbox.cc
        2. Зарегистрировать нового пользователя
        3. Сделать любой заказ
        4. Применить промокод "GIVEMEHALYAVA"
        5. Оформить заказ
        6. Оформить второй заказ с этим же промокодом

        Ожидаемый результат: При повторном применении промокода при оформлении заказа, промокод не применился
        """

        promo_code = 'GIVEMEHALYAVA'
        name = 'tese1324567123'
        email = 'tese1324574@test.com'
        password = 'test12345'

        first_name = 'Тестировщик'
        last_name = 'Тест'
        address = 'Комсомольская'
        city = 'Москва'
        state = 'Московская'
        postcode = '633010'
        number_phone = '8-999-999-9999'
        order_date = datetime.date.today() + datetime.timedelta(days=1)

        clear_data()
        go_to_url("http://pizzeria.skillbox.cc")
        with allure.step('Регистрация нового пользователя'):
            with allure.step('Открытие страницы "Мой аккаунт"'):
                find_element(By.XPATH, '//div[contains(@class, "store-menu")]'
                                       '//a[contains(text(), "Мой аккаунт")]').click()
            with allure.step('Поиск кнопки "Зарегистрироваться" и клик по ней'):
                find_element(By.CSS_SELECTOR, '[class=custom-register-button]').click()
            with allure.step(f'Поиск поля "Имя пользователя" и ввод значения "{name}"'):
                username_field = find_element(By.CSS_SELECTOR, '[id=reg_username]')
                username_field.send_keys(name)
            with allure.step(f'Поиск поля "Адрес почты" и ввод значения "{email}"'):
                email_field = find_element(By.CSS_SELECTOR, '[id=reg_email]')
                email_field.send_keys(email)
            with allure.step(f'Поиск поля "Пароль" и ввод значения "{password}"'):
                password_field = find_element(By.CSS_SELECTOR, '[id=reg_password]')
                password_field.send_keys(password)
            with allure.step('Поиск кнопки "Зарегистрироваться" и клик по ней'):
                find_element(By.CSS_SELECTOR, '[name=register]').click()
            with allure.step('Ожидание завершения регистрации'):
                wait_text_to_be_present_in_element(By.CSS_SELECTOR, '[class=content-page]', 'Регистрация завершена')
        with allure.step('Добавление товара в корзину'):
            with allure.step('Переход на главную страницу'):
                find_element(By.XPATH, '//div[contains(@class, "store-menu")]//a[contains(text(), "Главная")]').click()
            with allure.step('Ожидание загрузки всех товаров в слайдере'):
                product = wait_element_to_be_clickable(By.XPATH, '//li[contains(@class, "slick-active")]'
                                                                 '[contains(@data-slick-index, "3")]')
            moving_mouse_to_product(product)
            with allure.step('Поиск кнопки "В корзину" и клик по ней'):
                find_element(By.XPATH, '//li[contains(@class, "slick-active")]'
                                       '[contains(@data-slick-index, "3")]'
                                       '//a[contains(@class, "add_to_cart_button")]').click()
            with allure.step('Ожидание появления кнопки "Подробнее" и клик по ней'):
                wait_element_to_be_clickable(By.XPATH, '//li[contains(@class, "slick-active")]'
                                                       '[contains(@data-slick-index, "3")]'
                                                       '//a[contains(@class, "added_to_cart")]').click()
        with allure.step('Применение промокода'):
            with allure.step('Поиск поля "Введите код купона" и ввод значения'):
                promo_code_field = find_element(By.CSS_SELECTOR, '[name=coupon_code]')
                with allure.step(f'Ввод значения "{promo_code}"'):
                    promo_code_field.send_keys(promo_code)
            with allure.step('Поиск кнопки "Применить купон"'):
                promo_code_button = find_element(By.CSS_SELECTOR, '[name=apply_coupon]')
                with allure.step('Нажатие на кнопку "Применить купон"'):
                    promo_code_button.click()
                    time.sleep(2)
        with allure.step('Оформление заказа'):
            with allure.step('Поиск кнопки "Перейти к оплате" и клик по ней'):
                find_element(By.XPATH, '//*[contains(@class, "checkout-button")]').click()
            with allure.step('Заполнение обязательных полей'):
                with allure.step('Заполнение поля "Имя"'):
                    first_name_field = find_element(By.CSS_SELECTOR, '[id=billing_first_name]')
                    first_name_field.clear()
                    first_name_field.send_keys(first_name)
                with allure.step('Заполнение поля "Фамилия"'):
                    last_name_field = find_element(By.CSS_SELECTOR, '[id=billing_last_name]')
                    last_name_field.clear()
                    last_name_field.send_keys(last_name)
                with allure.step('Заполнение поля "Адрес"'):
                    address_field = find_element(By.CSS_SELECTOR, '[id=billing_address_1]')
                    address_field.clear()
                    address_field.send_keys(address)
                with allure.step('Заполнение поля "Город"'):
                    city_field = find_element(By.CSS_SELECTOR, '[id=billing_city]')
                    city_field.clear()
                    city_field.send_keys(city)
                with allure.step('Заполнение поля "Область"'):
                    state_field = find_element(By.CSS_SELECTOR, '[id=billing_state]')
                    state_field.clear()
                    state_field.send_keys(state)
                with allure.step('Заполнение поля "Индекс"'):
                    postcode_field = find_element(By.CSS_SELECTOR, '[id=billing_postcode]')
                    postcode_field.clear()
                    postcode_field.send_keys(postcode)
                with allure.step('Заполнение поля "Телефон"'):
                    phone_field = find_element(By.CSS_SELECTOR, '[id=billing_phone]')
                    phone_field.clear()
                    phone_field.send_keys(number_phone)
                with allure.step('Заполнение поля "Дата заказа"'):
                    find_element(By.CSS_SELECTOR, '[id=order_date]').send_keys(order_date.strftime('%d.%m.%Y'))
            with allure.step('Прокручивание страницы вниз'):
                selenium.execute_script("window.scrollTo(0, 1000)")
            with allure.step('Нажатие на кнопку "Оплата при доставке"'):
                wait_visibility_of_element_located(By.CSS_SELECTOR, '[id=payment_method_cod]').click()
            with allure.step('Нажатие на кнопку соглашения с политикой'):
                find_element(By.CSS_SELECTOR, '[id=terms]').click()
            with allure.step('Нажатие на кнопку "Оформить заказ"'):
                find_element(By.CSS_SELECTOR, '[id=place_order]').click()
            with allure.step('Ожидание завершения заказа'):
                time.sleep(5)
        with allure.step('Повторное добавление товара в корзину'):
            with allure.step('Переход на главную страницу'):
                find_element(By.XPATH, '//div[contains(@class, "store-menu")]//a[contains(text(), "Главная")]').click()
            with allure.step('Ожидание загрузки всех товаров в слайдере'):
                product = wait_element_to_be_clickable(By.XPATH, '//li[contains(@class, "slick-active")]'
                                                                 '[contains(@data-slick-index, "3")]')
            moving_mouse_to_product(product)
            with allure.step('Поиск кнопки "В корзину"'):
                button = find_element(By.XPATH, '//li[contains(@class, "slick-active")]'
                                                '[contains(@data-slick-index, "3")]'
                                                '//a[contains(@class, "add_to_cart_button")]')
            with allure.step('Нажатие на кнопку "В корзину"'):
                button.click()
            with allure.step('Ожидание появления кнопки "Подробнее"'):
                more = wait_element_to_be_clickable(By.XPATH, '//li[contains(@class, "slick-active")]'
                                                              '[contains(@data-slick-index, "3")]'
                                                              '//a[contains(@class, "added_to_cart")]')
            with allure.step('Нажатие на кнопку "Подробнее" для перехода в корзину'):
                more.click()
        with allure.step('Повторное применение промокода'):
            with allure.step('Поиск поля "Введите код купона" и ввод значения'):
                promo_code_field = find_element(By.CSS_SELECTOR, '[name=coupon_code]')
                with allure.step(f'Ввод значения "{promo_code}"'):
                    promo_code_field.send_keys(promo_code)
            with allure.step('Поиск кнопки "Применить купон"'):
                promo_code_button = find_element(By.CSS_SELECTOR, '[name=apply_coupon]')
                with allure.step('Нажатие на кнопку "Применить купон"'):
                    promo_code_button.click()
                    time.sleep(2)
        with allure.step('Проверка применения промокода'):
            with allure.step('Получение общей стоимости заказа'):
                total_cost = find_element(By.XPATH, '//*[contains(@class, "cart-subtotal")]'
                                                    '//span[contains(@class, "amount")]').text
            with allure.step('Получение суммы заказа'):
                amount = find_element(By.XPATH, '//*[contains(@class, "order-total")]'
                                                '//span[contains(@class, "amount")]').text
            with allure.step(f'Сравнение общей стоимости "{total_cost}" и суммы заказа "{amount}"'):
                if total_cost != amount:
                    raise ValueError(f'Сумма заказа "{amount}" отличается от общей стоимости "{total_cost}"')
