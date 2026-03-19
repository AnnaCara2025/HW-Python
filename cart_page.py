"""
Модуль содержит Page Object для страницы корзины.
"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Страница корзины
    """

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        """
        Инициализация страницы.

        :param driver: экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Нажать кнопку Checkout")
    def click_checkout(self) -> None:
        """Нажать кнопку Checkout."""
        button = self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON))
        button.click()