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
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # базовое ожидание для элементов

    def open(self):
        """Открыть страницу калькулятора"""
        self.driver.get(self.URL)

    def set_delay(self, seconds):
        """
        Установить задержку вычислений в секундах.
        Очищает поле и вводит новое значение.
        """
        delay_field = self.wait.until(
            EC.element_to_be_clickable(self.DELAY_INPUT)
        )
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, text):
        """
        Нажать на кнопку с указанным текстом (цифра, оператор, '=').
        """
        button_locator = (By.XPATH, self.BUTTON_TEMPLATE.format(text))
        button = self.wait.until(
            EC.element_to_be_clickable(button_locator)
        )
        button.click()

    def get_result(self):
        """
        Получить текущий текст на экране результата.
        """
        result_element = self.wait.until(
            EC.visibility_of_element_located(self.RESULT_SCREEN)
        )
        return result_element.text

    def wait_for_result(self, expected_value, timeout=46):
        """
        Ожидать, что результат станет равен ожидаемому значению.
        По умолчанию таймаут чуть больше задержки (45 сек).
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.RESULT_SCREEN, expected_value)
        )
