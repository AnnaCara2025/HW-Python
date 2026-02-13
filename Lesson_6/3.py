# Дождаться картинки
# 1. Перейдите на сайт https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
# 2. Дождитесь загрузки всех картинок.
# 3. Получите значение атрибута src у 3-й картинки.
# 4. Выведите значение в консоль.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

try:
    wait = WebDriverWait(driver, 90)
    
    # Ждем загрузки всех изображений (ожидаем 4)
    images = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#image-container img"))
    )
    
    # Ждем, пока у всех изображений появится src (не пустой)
    wait.until(
        lambda d: all(img.get_attribute("src") for img in 
        d.find_elements(By.CSS_SELECTOR, "#image-container img"))
    )
    
    # Получаем значение атрибута src у 3-й картинки (индекс 2)
    third_image = driver.find_elements(By.CSS_SELECTOR, "#image-container img")[2]
    src_value = third_image.get_attribute("src")
    
    print(f"Найдено изображений: {len(images)}")
    print(f"SRC 3-й картинки: {src_value}")
    
except Exception as e:
    print(f"Произошла ошибка: {e}")
    
finally:
    driver.quit()
