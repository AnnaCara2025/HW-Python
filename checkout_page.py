"""
Модуль содержит Page Object для страницы оформления заказа.
"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """
    Страница оформления заказа (Checkout: Your Information и Overview)
    """

    # Поля ввода информации
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    # Локаторы на странице Overview
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.ID, "finish")  # не используется в тесте, но может пригодиться

    def __init__(self, driver):
        """
        Инициализация страницы.

        :param driver: экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Ввести имя: {first_name}")
    def enter_first_name(self, first_name: str) -> None:
        """
        Ввести имя.

        :param first_name: имя
        :type first_name: str
        """
        element = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_INPUT))
        element.clear()
        element.send_keys(first_name)

    @allure.step("Ввести фамилию: {last_name}")
    def enter_last_name(self, last_name: str) -> None:
        """
        Ввести фамилию.

        :param last_name: фамилия
        :type last_name: str
        """
        element = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_INPUT))
        element.clear()
        element.send_keys(last_name)

    @allure.step("Ввести почтовый индекс: {postal_code}")
    def enter_postal_code(self, postal_code: str) -> None:
        """
        Ввести почтовый индекс.

        :param postal_code: почтовый индекс
        :type postal_code: str
        """
        element = self.wait.until(EC.element_to_be_clickable(self.POSTAL_CODE_INPUT))
        element.clear()
        element.send_keys(postal_code)

    @allure.step("Нажать Continue")
    def click_continue(self) -> None:
        """Нажать Continue (переход к Overview)."""
        button = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))
        button.click()

    @allure.step("Получить итоговую сумму")
    def get_total_amount(self) -> str:
        """
        Получить итоговую сумму (текст вида "Total: $58.29").

        :return: итоговая сумма в виде строки
        :rtype: str
        """
        total_element = self.wait.until(EC.visibility_of_element_located(self.TOTAL_LABEL))
        return total_element.text