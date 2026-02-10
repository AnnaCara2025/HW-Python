# Переименовать кнопку
# 1. Перейдите на сайт http://uitestingplayground.com/textinput.
# 2. Укажите в поле ввода текст SkyPro.
# 3. Нажмите на синюю кнопку.
# 4. Получите текст кнопки и выведите в консоль ("SkyPro").

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Инициализация драйвера и переход на страницу
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

try:
    wait = WebDriverWait(driver, 10)
    
    # 2. Указать в поле ввода текст SkyPro
    input_field = wait.until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )
    input_field.clear()
    input_field.send_keys("SkyPro")
    
    # 3. Нажать на синюю кнопку
    blue_button = driver.find_element(By.ID, "updatingButton")
    blue_button.click()
    
    # 4. Получить текст кнопки и вывести в консоль
    # Ждем обновления текста кнопки
    wait.until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )
    
    # Получаем и выводим текст кнопки
    button_text = driver.find_element(By.ID, "updatingButton").text
    print(button_text)  # "SkyPro"
    
except Exception as e:
    print(f"Произошла ошибка: {e}")
    
finally:
    driver.quit()