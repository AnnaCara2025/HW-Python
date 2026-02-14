# . Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html в Google Chrome.
# 2. В поле ввода по локатору #delay  введите значение 45.
# 3. Нажмите на кнопки:
# 7
# +
# 8
# =
# 4. Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    """Фикстура для инициализации браузера Chrome"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_slow_calculator(browser):
    """Тест медленного калькулятора с задержкой 45 секунд"""
    
    # 1. Открываем страницу
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # Увеличиваем время ожидания, так как калькулятор медленный
    wait = WebDriverWait(browser, 50)  # На 5 секунд больше чем 45
    
    # 2. Вводим значение 45 в поле задержки
    delay_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
    )
    delay_input.clear()
    delay_input.send_keys("45")
       
    # Нажимаем кнопку 7
    button_7 = browser.find_element(By.XPATH, "//span[text()='7']")
    button_7.click()
    
    # Нажимаем кнопку +
    button_plus = browser.find_element(By.XPATH, "//span[text()='+']")
    button_plus.click()
    
    # Нажимаем кнопку 8
    button_8 = browser.find_element(By.XPATH, "//span[text()='8']")
    button_8.click()
    
    # Нажимаем кнопку =
    button_equals = browser.find_element(By.XPATH, "//span[text()='=']")
    button_equals.click()
    
    # 4. Проверяем, что результат 15 отобразится через 45 секунд
    # Ждем пока результат не станет "15"
    result_element = wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
    
    # Получаем финальный результат для проверки
    result_display = browser.find_element(By.CLASS_NAME, "screen")
    final_result = result_display.text
    
    # Assert проверка
    assert final_result == "15", f"Ожидаемый результат '15', но получен '{final_result}'"
    

    print("Тест успешно пройден! Калькулятор показал результат 15 после 45 секунд.")
