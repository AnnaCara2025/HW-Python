"""
Модуль содержит Page Object для страницы медленного калькулятора.
"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Page Object для страницы медленного калькулятора:
    https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
    """

    # URL страницы
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    # Локаторы
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT_SCREEN = (By.CSS_SELECTOR, "#screen")
    # Кнопки будем искать динамически по тексту (XPATH)
    BUTTON_TEMPLATE = "//span[text()='{}']/.."  # родительский <button>

    def __init__(self, driver):
        """
        Инициализация страницы.

        :param driver: экземпляр WebDriver
        :type driver: selenium.webdriver.remote.webdriver.WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # базовое ожидание для элементов

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Открыть страницу калькулятора."""
        self.driver.get(self.URL)

    @allure.step("Установить задержку: {seconds} сек")
    def set_delay(self, seconds: int) -> None:
        """
        Установить задержку вычислений в секундах.
        Очищает поле и вводит новое значение.

        :param seconds: время задержки в секундах
        :type seconds: int
        """
        delay_field = self.wait.until(
            EC.element_to_be_clickable(self.DELAY_INPUT)
        )
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    @allure.step("Нажать кнопку: {text}")
    def click_button(self, text: str) -> None:
        """
        Нажать на кнопку с указанным текстом (цифра, оператор, '=').

        :param text: текст на кнопке
        :type text: str
        """
        button_locator = (By.XPATH, self.BUTTON_TEMPLATE.format(text))
        button = self.wait.until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()

    @allure.step("Получить результат с экрана")
    def get_result(self) -> str:
        """
        Получить текущий текст на экране результата.

        :return: значение на экране
        :rtype: str
        """
        result_element = self.wait.until(
            EC.visibility_of_element_located(self.RESULT_SCREEN)
        )
        return result_element.text

    @allure.step("Ожидать результат: {expected_value}")
    def wait_for_result(self, expected_value: str, timeout: int = 46) -> None:
        """
        Ожидать, что результат станет равен ожидаемому значению.
        По умолчанию таймаут чуть больше задержки (45 сек).

        :param expected_value: ожидаемое значение (строка)
        :type expected_value: str
        :param timeout: максимальное время ожидания в секундах
        :type timeout: int
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.RESULT_SCREEN, expected_value)
        )