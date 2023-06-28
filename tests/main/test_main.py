import datetime
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def adding_an_item_to_shopping_cart_in_slider(moving_mouse_to_product, wait_element_to_be_clickable, find_element):
    with allure.step('Добавление товара в корзину и переход в нее'):
        with allure.step('Ожидание загрузки всех товаров в слайдере'):
            product = wait_element_to_be_clickable(By.XPATH, '//li[contains(@class, "slick-active")]'
                                                             '[contains(@data-slick-index, "3")]')
            moving_mouse_to_product(product)
        with allure.step('Поиск кнопки "В корзину" и клик по ней'):
            find_element(By.XPATH, '//li[contains(@class, "slick-active")]'
                                   '[contains(@data-slick-index, "3")]'
                                   '//a[contains(@class, "add_to_cart_button")]').click()


def clicking_on_more_details_button(wait_element_to_be_clickable):
    with allure.step('Переход в корзину через нажатие на кнопку "Подробнее"'):
        wait_element_to_be_clickable(By.XPATH, '//li[contains(@class, "slick-active")]'
                                               '[contains(@data-slick-index, "3")]'
                                               '//a[contains(@class, "added_to_cart")]').click()


def opening_page_via_main_menu(find_element, page):
    with allure.step(f'Открытие страницы "{page}" через главное меню'):
        find_element(By.XPATH, f'//div[contains(@class, "store-menu")]//a[contains(text(), "{page}")]').click()


def waiting_for_all_products_to_load_in_slider(wait_element_to_be_clickable):
    with allure.step('Ожидание загрузки всех товаров в слайдере'):
        product = wait_element_to_be_clickable(By.XPATH, '//li[contains(@class, "slick-active")]'
                                                         '[contains(@data-slick-index, "3")]')
    return product


def clicking_on_add_to_cart_button(find_element):
    with allure.step('Поиск кнопки "В корзину" и клик по ней'):
        find_element(By.CSS_SELECTOR, '[name=add-to-cart]').click()


def clicking_on_add_to_go_to_payment(find_element):
    with allure.step('Поиск кнопки "Перейти к оплате" и клик по ней'):
        find_element(By.XPATH, '//*[contains(@class, "checkout-button")]').click()


def getting_cost_of_product_in_cart(find_element):
    with allure.step('Получение стоимости товара в корзине'):
        cost_product_in_basket = find_element(By.XPATH, '//*[contains(@class, "product-price")]'
                                                        '//span[contains(@class, "amount")]').text[:-4]
    return cost_product_in_basket


@allure.feature('Тестирование основного флоу')
class TestMainFlow:
    @allure.title('Добавление товара в корзину при нажатии на кнопку "В корзину" в слайдере')
    def test_adding_item_cart_from_slider(self,
                                          go_to_url,
                                          clear_data,
                                          moving_mouse_to_product,
                                          wait_element_to_be_clickable,
                                          wait_text_to_be_present_in_element,
                                          find_element,
                                          selenium):
        """
        Шаги:
        1. Открыть страницу http://pizzeria.skillbox.cc
        2. Навести мышку на любой товар в слайдере с пиццами
        3. Нажать на кнопку "В корзину"

        Ожидаемый результат: После наведения мышки на товар, появилась кнопка "В корзину"
        При нажатии на кнопку "В корзину" товар добавился в корзину
        В правом в верхнем углу, возле иконки корзины, изменилась сумма заказа
        """

        clear_data()
        go_to_url("http://pizzeria.skillbox.cc")
        adding_an_item_to_shopping_cart_in_slider(moving_mouse_to_product, wait_element_to_be_clickable, find_element)
        with allure.step('Проверка добавления товара в корзину'):
            with allure.step('Получение стоимости товара в слайдере'):
                cost_product = find_element(By.XPATH, '//li[contains(@class, "slick-active")]'
                                                      '[contains(@data-slick-index, "3")]'
                                                      '//span[contains(@class, "amount")]').text
            with allure.step('Проверка, что в корзине изменилась сумма'):
                wait_text_to_be_present_in_element(By.XPATH,
                                                   '//a[contains(@title, "View your shopping cart")]', cost_product)

    @allure.title('Переключение слайдера с пиццами')
    def test_switching_slider(self,
                              go_to_url,
                              clear_data,
                              moving_mouse_to_product,
                              wait_element_to_be_clickable):
        """
        Шаги:
        1. Открыть страницу http://pizzeria.skillbox.cc
        2. Навести мышку на слайдер с пиццами
        3. Нажать с правой стороны слайдера на кнопку "Вправо"
        4. Нажать с левой стороны слайдера на кнопку "Влево"

        Ожидаемый результат: После наведения мышки на слайдер,
        появились кнопки для переключения слайдера вправо или влево
        При нажатии на кнопку "Вправо" слайдер переключился вперед
        При нажатии на кнопку "Влево" слайдер переключился назад
        """

        clear_data()
        go_to_url("http://pizzeria.skillbox.cc")
        product = waiting_for_all_products_to_load_in_slider(wait_element_to_be_clickable)
        moving_mouse_to_product(product)
        with allure.step('Переключение слайдера вперед'):
            wait_element_to_be_clickable(By.CSS_SELECTOR, '[aria-label=next]').click()
            with allure.step('Проверка, что слайдер переключился вперед'):
                wait_element_to_be_clickable(By.XPATH, '//*[contains(@class, "prod1-slider")]'
                                                       '//li[contains(@class, "slick-active")]'
                                                       '[contains(@data-slick-index, "4")]//h3')
        moving_mouse_to_product(product)
        with allure.step('Переключение слайдера назад'):
            wait_element_to_be_clickable(By.CSS_SELECTOR, '[aria-label=previous]').click()
            with allure.step('Проверка, что слайдер переключился назад'):
                wait_element_to_be_clickable(By.XPATH, '//*[contains(@class, "prod1-slider")]'
                                                       '//li[contains(@class, "slick-active")]'
                                                       '[contains(@data-slick-index, "0")]//h3')

    @allure.title('Открытие страницы товара из слайдера')
    def test_opening_product_page_from_slider(self,
                                              go_to_url,
                                              clear_data,
                                              wait_element_to_be_clickable,
                                              find_element):
        """
        Шаги:
        1. Открыть страницу http://pizzeria.skillbox.cc
        2. Навести мышку на картинку любой пиццы в слайдере
        3. Нажать на картинку пиццы

        Ожидаемый результат: Открылась страница с описанием товара выбранного товара
        """

        clear_data()
        go_to_url("http://pizzeria.skillbox.cc")
        with allure.step('Ожидание загрузки всех товаров в слайдере'):
            waiting_for_all_products_to_load_in_slider(wait_element_to_be_clickable)
        with allure.step('Получение названия товара в слайдере'):
            product = find_element(By.XPATH, '//li[contains(@class, "slick-active")]'
                                             '[contains(@data-slick-index, "3")]//h3')
            name = product.text.lower()
        with allure.step('Переход на страницу товара'):
            product.click()
        with allure.step('Проверка, что открылась верная страница с товаром'):
            with allure.step('Получение названия товара на странице товара'):
                product_title = find_element(By.CSS_SELECTOR, '[class="product_title entry-title"]').text.lower()
            with allure.step('Проверка открытой страницы'):
                if product_title != name:
                    raise ValueError(f'Открыта неверная страница, ожидалось {name}, а открылась {product_title}')

    @allure.title('Выбор дополнительных опций товара и добавление в корзину')
    def test_selecting_additional_product_options(self,
                                                  go_to_url,
                                                  clear_data,
                                                  wait_element_to_be_clickable,
                                                  find_element,
                                                  wait_text_to_be_present_in_element):
        """
        Шаги:
        1. Открыть страницу http://pizzeria.skillbox.cc
        2. Навести мышку на картинку любой пиццы в слайдере
        3. Нажать на картинку пиццы
        4. Выбрать в "Выбор борта для пиццы" - "Сырный"
        5. Нажать на кнопку "В корзину"

        Ожидаемый результат: При выборе дополнительной опции, сумма товара возрастает на ту сумму, сколько стоит опция
        После нажатия на кнопку "В корзину" товар добавился в корзину с указанной суммой
        """

        clear_data()
        go_to_url("http://pizzeria.skillbox.cc")
        product = waiting_for_all_products_to_load_in_slider(wait_element_to_be_clickable)
        product.click()
        with allure.step('Получение стоимости товара без доп.опции'):
            initial_cost = find_element(By.XPATH, '//div[contains(@class, "summary")]'
                                                  '//span[contains(@class, "amount")]').text[:-4]
        with allure.step('Получение стоимости доп.опции'):
            cost_additional_option = find_element(By.XPATH,
                                                  '//*[contains(text(), "Сырный")]').get_attribute('value')[:-3]
        with allure.step('Поиск доп.опции "Сырный" и клик по ней'):
            find_element(By.XPATH, '//*[contains(text(), "Сырный")]').click()
        with allure.step('Получение стоимости товара с доп.опцией'):
            total_cost = find_element(By.XPATH, '//div[contains(@class, "summary")]'
                                                '//span[contains(@class, "amount")]').text[:-4]
        with allure.step('Проверка стоимости товара'):
            check_cost = int(initial_cost) + int(cost_additional_option)
            if check_cost != int(total_cost):
                raise ValueError('Стоимость товара не соответствует цене')
        with allure.step('Добавление товара в корзину'):
            find_element(By.CSS_SELECTOR, '[name=add-to-cart]').click()
        with allure.step('Проверка, что товар добавлен в корзину с нужной стоимостью'):
            wait_text_to_be_present_in_element(By.XPATH, '//a[contains(@title, "View your shopping cart")]', total_cost)

    @allure.title('Изменение количества товара на странице товара и добавление в корзину')
    def test_changing_quantity_product_on_product_page(self,
                                                       go_to_url,
                                                       clear_data,
                                                       wait_element_to_be_clickable,
                                                       find_element):
        """
        Шаги:
        1. Открыть страницу http://pizzeria.skillbox.cc
        2. Навести мышку на любую пиццу в слайдере
        3. Нажать на картинку пиццы
        4. Изменить кол-во товара на "2"
        5. Нажать на кнопку "В корзину"
        6. Нажать на ссылку "Корзина" в меню сайта

        Ожидаемый результат: В корзине присутствует товар в количестве "2", общая стоимость рассчитана за 2 товара
        """

        clear_data()
        go_to_url("http://pizzeria.skillbox.cc")
        product = waiting_for_all_products_to_load_in_slider(wait_element_to_be_clickable)
        product.click()
        with allure.step('Получение стоимости товара на странице товара'):
            cost_product_on_product_page = find_element(By.XPATH, '//div[contains(@class, "summary")]'
                                                                  '//span[contains(@class, "amount")]').text[:-4]
        with allure.step('Поиск поля "Количество" и ввод значения'):
            el = find_element(By.CSS_SELECTOR, '[title="Кол-во"]')
            el.clear()
            el.send_keys('2')
        clicking_on_add_to_cart_button(find_element)
        opening_page_via_main_menu(find_element, 'Корзина')
        cost_product_in_basket = getting_cost_of_product_in_cart(find_element)
        with allure.step('Проверка стоимости товара'):
            if cost_product_in_basket != cost_product_on_product_page:
                raise ValueError('Стоимость товара не соответствует')
        with allure.step('Проверка количества товара'):
            quantity_in_basket = find_element(By.CSS_SELECTOR, '[title="Кол-во"]').get_attribute('value')
            if quantity_in_basket != '2':
                raise ValueError('Количество товара не соответствует')
        with allure.step('Проверка общей стоимости товара'):
            total_cost_product_in_basket = find_element(By.XPATH, '//*[contains(@class, "product-subtotal")]'
                                                                  '//span[contains(@class, "amount")]').text[:-4]
            if total_cost_product_in_basket != str(int(cost_product_in_basket) * 2):
                raise ValueError('Общая стоимость товара не соответствует')

    @allure.title('Увеличение количества товара в корзине')
    def test_increasing_quantity_goods_in_basket(self,
                                                 go_to_url,
                                                 clear_data,
                                                 wait_element_to_be_clickable,
                                                 find_element,
                                                 wait_text_to_be_present_in_element):
        """
        Шаги:
        1. Открыть страницу http://pizzeria.skillbox.cc
        2. Навести мышку на любую пиццу в слайдере
        3. Нажать на картинку пиццы
        4. Нажать на кнопку "В корзину"
        5. Нажать на ссылку "Корзина" в меню сайта
        6. В колонке "Количество" изменить на "3"
        7. Нажать на кнопку "Обновить корзину"

        Ожидаемый результат: Количество товара изменилось на 3, общая стоимость товара пересчиталась
        """

        quantity_goods = 3

        clear_data()
        go_to_url("http://pizzeria.skillbox.cc")
        with allure.step('Добавление товара в корзину и переход в нее'):
            product = waiting_for_all_products_to_load_in_slider(wait_element_to_be_clickable)
            product.click()
            clicking_on_add_to_cart_button(find_element)
            opening_page_via_main_menu(find_element, 'Корзина')
        cost_product_in_basket = getting_cost_of_product_in_cart(find_element)
        with allure.step('Поиск поля "Количество" и замена значения'):
            el = find_element(By.CSS_SELECTOR, '[title="Кол-во"]')
            el.clear()
            el.send_keys(quantity_goods)
        with allure.step('Поиск кнопки "Обновить корзину" и клик по ней'):
            find_element(By.CSS_SELECTOR, '[name="update_cart"]').click()
        with allure.step('Проверка количества товара и общей стоимости'):
            with allure.step('Получение общей стоимости товара'):
                total_cost_product_in_basket = int(cost_product_in_basket) * quantity_goods
            with allure.step('Ожидание замены общей стоимости товара'):
                wait_text_to_be_present_in_element(By.XPATH, '//*[contains(@class, "product-subtotal")]'
                                                             '//span[contains(@class, "amount")]',
                                                   str(total_cost_product_in_basket))

    @allure.title('Удаление товара из корзины')
    def test_removing_an_item_from_shopping_cart(self,
                                                 go_to_url,
                                                 clear_data,
                                                 wait_element_to_be_clickable,
                                                 find_element,
                                                 wait_text_to_be_present_in_element):
        """
        Шаги:
        1. Открыть страницу http://pizzeria.skillbox.cc
        2. Навести мышку на любую пиццу в слайдере
        3. Нажать на картинку пиццы
        4. Нажать на кнопку "В корзину"
        5. Нажать на ссылку "Корзина" в меню сайта
        6. Нажать на кнопку "Х" слева в таблице

        Ожидаемый результат: Выбранный товар удалился из корзины
        """

        clear_data()
        go_to_url("http://pizzeria.skillbox.cc")
        with allure.step('Добавление товара в корзину и переход в нее'):
            product = waiting_for_all_products_to_load_in_slider(wait_element_to_be_clickable)
            product.click()
            clicking_on_add_to_cart_button(find_element)
            opening_page_via_main_menu(find_element, 'Корзина')
        with allure.step('Получение имени товара в корзине'):
            product_name = find_element(By.XPATH, '//*[contains(@class, "product-name")]/a').text
        with allure.step('Удаление товара из корзины'):
            find_element(By.CSS_SELECTOR, '[class="remove"]').click()
        with allure.step('Проверка, что товар удален из корзины'):
            wait_text_to_be_present_in_element(By.CSS_SELECTOR, '[role=alert]', product_name)

    @allure.title('Переход в раздел "Десерты"')
    def test_go_to_desserts_section(self,
                                    go_to_url,
                                    clear_data,
                                    moving_mouse_to_product,
                                    wait_element_to_be_clickable,
                                    find_element,
                                    selenium):
        """
        Шаги:
        1. Открыть страницу http://pizzeria.skillbox.cc
        2. В меню сайта навести мышку на "Меню"
        3. В выпадающем списке нажать на "Десерты"

        Ожидаемый результат: Открылась страница меню "Десерты"
        """

        page = 'Десерты'

        clear_data()
        go_to_url("http://pizzeria.skillbox.cc")
        with allure.step('Поиск ссылки "Меню" в главном меню'):
            element = wait_element_to_be_clickable(By.XPATH, '//*[contains(@class, "menu-item-has-children")]')
        moving_mouse_to_product(element)
        with allure.step('Поиск ссылки "Десерты" в подменю и клик по ней'):
            find_element(By.XPATH, f'//*[contains(text(), "{page}")]').click()
        with allure.step('Поиск заголовка страницы и получение значения'):
            title = find_element(By.XPATH, '//*[contains(@class, "entry-title ak-container")]').text.islower()
        with allure.step('Проверка заголовка страницы'):
            if title != page.islower():
                raise ValueError('Заголовок страницы не соответствует')

    @allure.title('Фильтрация товаров по цене')
    def test_filtering_products_by_price(self,
                                         go_to_url,
                                         clear_data,
                                         find_element,
                                         find_elements,
                                         selenium):
        """
        Шаги:
        1. Открыть страницу http://pizzeria.skillbox.cc/product-category/menu/deserts
        2. В фильтре "Цена" изменить диапазон цен на "110-140"
        3. Нажать на кнопку "Применить"

        Ожидаемый результат: В списке отображаются десерты по заданному фильтру.
        """

        clear_data()
        go_to_url("http://pizzeria.skillbox.cc/product-category/menu/deserts")
        with allure.step('Изменение диапазона фильтра'):
            with allure.step('Поиск правой кнопки фильтра'):
                right_button = find_element(By.XPATH, '//*[contains(@style, "left: 100%;")]')
            with allure.step('Перемещение правой кнопки на значение 140'):
                action_chains = webdriver.ActionChains(selenium)
                action_chains \
                    .click_and_hold(right_button) \
                    .move_by_offset(xoffset=-200, yoffset=0) \
                    .perform()
                action_chains.release().perform()
            with allure.step('Поиск кнопки "Применить" и клик по ней'):
                find_element(By.XPATH, '//div[contains(@class, "price_slider_amount")]/child::button').click()
        with allure.step('Проверка товаров в списке по заданному фильтру'):
            with allure.step('Получение всех товаров в списке'):
                price_goods = find_elements(By.XPATH, '//*[contains(@class, "price-cart")]'
                                                      '//span[contains(@class, "amount")]')
            with allure.step('Проверка суммы товара'):
                for i in price_goods:
                    price = int(i.text[:-4])
                    if price > 140:
                        raise ValueError(f'Сумма товара "{price}" превышает заданному фильтру')

    @allure.title('Оформление заказа без авторизации')
    def test_making_an_order_without_authorization(self,
                                                   go_to_url,
                                                   clear_data,
                                                   wait_element_to_be_clickable,
                                                   wait_text_to_be_present_in_element,
                                                   find_element,
                                                   selenium):
        """
        Шаги:
        1. Открыть страницу http://pizzeria.skillbox.cc
        2. Навести мышку на любую пиццу в слайдере с пиццами
        3. Нажать на кнопку "В корзину"
        4. Нажать на кнопку "Подробнее"
        5. Нажать на кнопку "Перейти к оплате"

        Ожидаемый результат: Открылась страница с просьбой авторизоваться
        """

        clear_data()
        go_to_url("http://pizzeria.skillbox.cc")
        adding_an_item_to_shopping_cart_in_slider(wait_element_to_be_clickable, find_element, selenium)
        clicking_on_more_details_button(wait_element_to_be_clickable)
        clicking_on_add_to_go_to_payment(find_element)
        with allure.step('Ожидание появления текста о необходимости авторизоваться'):
            wait_text_to_be_present_in_element(By.XPATH, '//div[contains(@class, "content-page")]/child::div',
                                               'Для оформления заказа необходимо авторизоваться.')

    @allure.title('Регистрация аккаунта')
    def test_account_registration(self,
                                  go_to_url,
                                  clear_data,
                                  wait_text_to_be_present_in_element,
                                  find_element):
        """
        Шаги:
        1. Открыть страницу http://pizzeria.skillbox.cc
        2. В меню сайта нажать на ссылку "Мой аккаунт"
        3. Нажать на кнопку "Зарегистрироваться"
        4. В поле "Имя пользователя" ввести валидное имя латинскими буквами
        5. В поле "Адрес почты" ввести валидный email
        6. В поле "Пароль" ввести валидный пароль латинскими буквами, цифрами, спецсимволами
        7. Нажать на кнопку "Зарегистрироваться"
        8. В меню сайта нажать на ссылку "Мой аккаунт"

        Ожидаемый результат: Пользователь авторизован в личном кабинете
        """

        name = 'tes13245679'
        email = 'tes1324569@test.com'
        password = 'test12345'

        clear_data()
        go_to_url("http://pizzeria.skillbox.cc")
        opening_page_via_main_menu(find_element, 'Мой аккаунт')
        with allure.step('Поиск кнопки "Зарегистрироваться" и клик по ней'):
            find_element(By.CSS_SELECTOR, '[class=custom-register-button]').click()
        with allure.step(f'Поиск поля "Имя пользователя" и ввод значения "{name}"'):
            name_field = find_element(By.CSS_SELECTOR, '[id=reg_username]')
            name_field.send_keys(name)
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
        opening_page_via_main_menu(find_element, 'Мой аккаунт')
        with allure.step('Проверка авторизации'):
            check = find_element(By.XPATH, '(//div[contains(@class, "woocommerce-MyAccount-content")]'
                                           '/child::p)[1]').text
            if name not in check:
                raise ValueError('Пользователь не авторизован')

    @allure.title('Оформление заказа с авторизацией')
    def test_making_an_order_with_authorization(self,
                                                go_to_url,
                                                clear_data,
                                                wait_element_to_be_clickable,
                                                wait_visibility_of_element_located,
                                                find_element,
                                                selenium):
        """
        Шаги:
        1. Открыть страницу http://pizzeria.skillbox.cc
        2. В меню сайта нажать на ссылку "Мой аккаунт"
        3. В поле "Имя пользователя или почта" ввести зарегистрированное имя пользователя
        4. В поле "Пароль" ввести валидный пароль от зарегистрированного пользователя
        5. Нажать на кнопку "Войти"
        6. В меню сайта нажать на ссылку "Главная"
        7. Навести мышку на любую пиццу в слайдере с пиццами
        8. Нажать на кнопку "В корзину"
        9. Нажать на кнопку "Подробнее"
        10. Нажать на кнопку "Перейти к оплате"
        11. Заполнить все обязательные поля валидными значениями
        12. В поле "Оплата" выбрать "Оплата при доставке"
        13. В поле "Дата" выбрать завтрашний день
        14. Нажать на чекбокс политики
        15. Нажать на кнопку "Оформить заказ"

        Ожидаемый результат: Открылась страница с деталями заказа, общая сумма и личные данные верны
        """

        username = 'test13245678'
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
        with allure.step('Авторизация пользователя'):
            opening_page_via_main_menu(find_element, 'Мой аккаунт')
            with allure.step(f'Поиск поля "Имя пользователя или почта" и ввод значения "{username}"'):
                username_field = find_element(By.CSS_SELECTOR, '[id=username]')
                username_field.send_keys(username)
            with allure.step(f'Поиск поля "Пароль" и ввод значения "{password}"'):
                password_field = find_element(By.CSS_SELECTOR, '[id=password]')
                password_field.send_keys(password)
            with allure.step('Поиск кнопки "Войти" и клик по ней'):
                find_element(By.CSS_SELECTOR, '[name=login]').click()
        with allure.step('Добавление товара в корзину'):
            opening_page_via_main_menu(find_element, 'Главная')
            adding_an_item_to_shopping_cart_in_slider(wait_element_to_be_clickable, find_element, selenium)
            clicking_on_more_details_button(wait_element_to_be_clickable)
        with allure.step('Оформление заказа'):
            clicking_on_add_to_go_to_payment(find_element)
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
                selenium.execute_script("window.scrollTo(0, 1500)")
            with allure.step('Нажатие на кнопку "Оплата при доставке"'):
                wait_visibility_of_element_located(By.CSS_SELECTOR, '[id=payment_method_cod]').click()
            with allure.step('Нажатие на кнопку соглашения с политикой'):
                find_element(By.CSS_SELECTOR, '[id=terms]').click()
            with allure.step('Получение суммы заказа'):
                amount = find_element(By.XPATH, '//*[contains(@class, "order-total")]'
                                                '//span[contains(@class, "amount")]').text
            with allure.step('Нажатие на кнопку "Оформить заказ"'):
                find_element(By.CSS_SELECTOR, '[id=place_order]').click()
            with allure.step('Ожидание завершения заказа'):
                time.sleep(5)
        with allure.step('Проверка деталей заказа'):
            with allure.step('Получение суммы заказа в деталях заказа'):
                total_cost = find_element(By.XPATH, '//ul[contains(@class, "order_details")]'
                                                    '//li[contains(@class, "total")]'
                                                    '//span[contains(@class, "amount")]').text
            with allure.step('Получение деталей заказа'):
                order_details = find_element(By.XPATH, '//*[contains(@class, "customer-details")]//address').text
                if total_cost != amount:
                    raise ValueError(f'Сумма заказа "{total_cost}" в деталях отличается '
                                     f'от суммы заказа при оформлении "{amount}"')
                words = [last_name, first_name, address, city, state, postcode, number_phone]
                for word in words:
                    if word not in order_details:
                        raise ValueError(f'Детали заказа не соответствует заполненному полю "{word}"')
