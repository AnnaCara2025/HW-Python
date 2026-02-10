# 1. Откройте сайт магазина: https://www.saucedemo.com/ в FireFox.
# 2. Авторизуйтесь как пользователь standard_user.
# 3. Добавьте в корзину товары:
# Sauce Labs Backpack.
# Sauce Labs Bolt T-Shirt.
# Sauce Labs Onesie.
# 4. Перейдите в корзину.
# 5. Нажмите Checkout.
# 6. Заполните форму своими данными: 
# имя,
# фамилия,
# почтовый индекс.
# 7. Нажмите кнопку Continue.
# 8. Прочитайте со страницы итоговую стоимость (Total).
# 9. Закройте браузер.
# 10. Проверьте, что итоговая сумма равна $58.29.


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    """Фикстура для инициализации и закрытия браузера Firefox"""
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_checkout_total_amount(browser):
    """Тест проверки итоговой стоимости товаров в корзине"""
    
    # 1. Открываем сайт магазина
    browser.get("https://www.saucedemo.com/")
    
    # Инициализируем ожидание
    wait = WebDriverWait(browser, 10)
    
    # 2. Авторизуемся как пользователь standard_user
    # Ждем появления поля для ввода логина
    username_field = wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    username_field.send_keys("standard_user")
    
    # Вводим пароль
    password_field = browser.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")
    
    # Нажимаем кнопку входа
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()
    
    # Ждем загрузки страницы с товарами после авторизации
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    
    # 3. Добавляем товары в корзину
    # Список товаров для добавления
    products_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt", 
        "Sauce Labs Onesie"
    ]
    
    for product_name in products_to_add:
        # Находим кнопку "Add to cart" для конкретного товара
        # Используем XPath для поиска кнопки по названию товара
        add_button = browser.find_element(
            By.XPATH, 
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item_description']//button"
        )
        add_button.click()
    
    # 4. Переходим в корзину
    cart_icon = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()
    
    # Ждем загрузки страницы корзины
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
    )
    
    # 5. Нажимаем Checkout
    checkout_button = browser.find_element(By.ID, "checkout")
    checkout_button.click()
    
    # 6. Заполняем форму данными
    # Ждем появления формы
    wait.until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    
    # Заполняем имя
    first_name_field = browser.find_element(By.ID, "first-name")
    first_name_field.send_keys("Иван")
    
    # Заполняем фамилию
    last_name_field = browser.find_element(By.ID, "last-name")
    last_name_field.send_keys("Иванов")
    
    # Заполняем почтовый индекс
    postal_code_field = browser.find_element(By.ID, "postal-code")
    postal_code_field.send_keys("123456")
    
    # 7. Нажимаем кнопку Continue
    continue_button = browser.find_element(By.ID, "continue")
    continue_button.click()
    
    # 8. Читаем итоговую стоимость (Total)
    # Ждем появления элемента с итоговой стоимостью
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    
    total_element = browser.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text
    
    # Извлекаем числовое значение из текста (формат "Total: $58.29")
    total_value = total_text.split("$")[1] if "$" in total_text else total_text
    
    # 10. Проверяем, что итоговая сумма равна $58.29
    # Браузер закроется автоматически через фикстуру после завершения теста
    assert total_value == "58.29", f"Итоговая сумма должна быть $58.29, но получено ${total_value}"