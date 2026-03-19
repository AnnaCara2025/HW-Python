"""
Модуль содержит Page Object для главной страницы с товарами.
"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """
    Главная страница с товарами (после логина)
    """

    # Локатор для кнопки добавления товара в корзину по имени товара
    ADD_TO_CART_BUTTON_TEMPLATE = "//div[text()='{}']/ancestor::div[@class='inventory_item']//button"
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        """
        Инициализация страницы.

        :param driver: экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавить товар в корзину: {item_name}")
    def add_item_to_cart(self, item_name: str) -> None:
        """
        Добавить товар в корзину по его названию.
        Например: "Sauce Labs Backpack"

        :param item_name: название товара
        :type item_name: str
        """
        button_locator = (By.XPATH, self.ADD_TO_CART_BUTTON_TEMPLATE.format(item_name))
        button = self.wait.until(EC.element_to_be_clickable(button_locator))
        # Кнопка может содержать текст "Add to cart" или уже "Remove"
        if "Add to cart" in button.text:
            button.click()
        # Если уже добавлен, можно пропустить, но для теста будем добавлять впервые

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Перейти в корзину (кликнуть на иконку корзины)."""
        cart_link = self.wait.until(EC.element_to_be_clickable(self.CART_LINK))
        cart_link.click()
