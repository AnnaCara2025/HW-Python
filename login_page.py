"""
Модуль содержит Page Object для страницы авторизации.
"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Страница авторизации https://www.saucedemo.com/
    """

    # Локаторы
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        """
        Инициализация страницы.

        :param driver: экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу авторизации")
    def open(self) -> None:
        """Открыть страницу авторизации."""
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Ввести логин: {username}")
    def enter_username(self, username: str) -> None:
        """
        Ввести логин.

        :param username: логин
        :type username: str
        """
        element = self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT))
        element.clear()
        element.send_keys(username)

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> None:
        """
        Ввести пароль (значение не логируется в целях безопасности).

        :param password: пароль
        :type password: str
        """
        element = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT))
        element.clear()
        element.send_keys(password)

    @allure.step("Нажать кнопку Login")
    def click_login(self) -> None:
        """Нажать кнопку Login."""
        element = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        element.click()