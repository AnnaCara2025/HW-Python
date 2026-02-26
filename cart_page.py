from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    """
    Страница корзины
    """

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):
        """Нажать кнопку Checkout"""
        button = self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON))
        button.click()