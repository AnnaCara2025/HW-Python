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
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_item_to_cart(self, item_name):
        """
        Добавить товар в корзину по его названию.
        Например: "Sauce Labs Backpack"
        """
        button_locator = (By.XPATH, self.ADD_TO_CART_BUTTON_TEMPLATE.format(item_name))
        button = self.wait.until(EC.element_to_be_clickable(button_locator))
        # Кнопка может содержать текст "Add to cart" или уже "Remove"
        if "Add to cart" in button.text:
            button.click()
        # Если уже добавлен, можно пропустить, но для теста будем добавлять впервые

    def go_to_cart(self):
        """Перейти в корзину (кликнуть на иконку корзины)"""
        cart_link = self.wait.until(EC.element_to_be_clickable(self.CART_LINK))
        cart_link.click()