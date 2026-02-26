import pytest
from selenium import webdriver
from calculator_page import CalculatorPage

@pytest.fixture
def driver():
    """Фикстура для управления драйвером браузера"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_slow_calculator(driver):
    """
    Тест проверяет работу калькулятора с задержкой 45 секунд:
    7 + 8 = 15.
    """
    # Создаём объект страницы
    page = CalculatorPage(driver)

    # Открываем страницу
    page.open()

    # Устанавливаем задержку 45 секунд
    page.set_delay(45)

    # Выполняем вычисления: 7 + 8 =
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    # Ожидаем появления результата 15 (максимум 46 секунд)
    page.wait_for_result("15", timeout=46)

    # Дополнительно проверяем точное совпадение
    assert page.get_result() == "15", "Результат вычислений неверен"