"""
Тесты для проверки медленного калькулятора.
"""
import allure
import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    """Фикстура для управления драйвером браузера."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Calculator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест медленного калькулятора: 7 + 8 = 15")
@allure.description("Проверяет работу калькулятора с задержкой 45 секунд.")
def test_slow_calculator(driver):
    """
    Тест проверяет работу калькулятора с задержкой 45 секунд:
    7 + 8 = 15.
    """
    # Создаём объект страницы
    page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        page.open()

    with allure.step("Установить задержку 45 секунд"):
        page.set_delay(45)

    with allure.step("Выполнить вычисления: 7 + 8 ="):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Ожидать появления результата 15"):
        page.wait_for_result("15", timeout=46)

    with allure.step("Проверить, что результат равен 15"):
        assert page.get_result() == "15", "Результат вычислений неверен"
