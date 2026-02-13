# Нажать на кнопку
# 1. Перейдите на страницу http://uitestingplayground.com/ajax.
# 2. Нажмите на синюю кнопку.
# 3. Получите текст из зеленой плашки.
# 4. Выведите его в консоль ("Data loaded with AJAX get request.").

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Инициализация драйвера и переход на страницу
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

try:
    # 2. Нажатие на синюю кнопку (более специфичный локатор)
    blue_button = driver.find_element(By.ID, "ajaxButton")
    blue_button.click()
    
    # 3. Ожидание появления текста из зеленой плашки
    wait = WebDriverWait(driver, 20)
    
    # Сначала дожидаемся, что элемент станет видимым
    green_banner = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )
    
    # 4. Получение текста и вывод в консоль
    result_text = green_banner.text
    print(result_text)  # "Data loaded with AJAX get request."

except Exception as e:
    print(f"Произошла ошибка: {e}")
    
finally:
    driver.quit()
