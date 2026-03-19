"""
Тесты для проверки оформления заказа на Saucedemo.
"""
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    """Фикстура для управления драйвером Firefox."""
    # Если geckodriver не в PATH, укажите путь: Service('/path/to/geckodriver')
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Shop")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Оформление заказа с тремя товарами")
@allure.description("Проверка полного сценария покупки: авторизация, добавление товаров, "
                    "заполнение формы, проверка итоговой суммы.")
def test_saucedemo_purchase(driver):
    """
    Тест проверяет оформление заказа с тремя товарами и итоговую сумму.
    """
    # Данные для авторизации
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"

    # Данные для формы
    FIRST_NAME = "Иван"
    LAST_NAME = "Петров"
    POSTAL_CODE = "123456"

    # Список товаров для добавления
    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    # Ожидаемая итоговая сумма
    expected_total = "Total: $58.29"

    with allure.step("Авторизация на сайте"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username(USERNAME)
        login_page.enter_password(PASSWORD)
        login_page.click_login()

    with allure.step("Добавление товаров в корзину"):
        inventory_page = InventoryPage(driver)
        for item in items:
            inventory_page.add_item_to_cart(item)

    with allure.step("Переход в корзину"):
        inventory_page.go_to_cart()

    with allure.step("Переход к оформлению заказа"):
        cart_page = CartPage(driver)
        cart_page.click_checkout()

    with allure.step("Заполнение формы информации"):
        checkout_page = CheckoutPage(driver)
        checkout_page.enter_first_name(FIRST_NAME)
        checkout_page.enter_last_name(LAST_NAME)
        checkout_page.enter_postal_code(POSTAL_CODE)
        checkout_page.click_continue()

    with allure.step("Получение итоговой суммы"):
        actual_total = checkout_page.get_total_amount()

    with allure.step("Проверка итоговой суммы"):
        assert actual_total == expected_total, \
            f"Ожидалось {expected_total}, получено {actual_total}"