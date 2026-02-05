# Задание:
# 1. Открыть браузер Firefox
# 2. Перейти на страницу: http://the-internet.herokuapp.com/inputs
# 3. Ввести в поле текст "Sky"
# 4. Очистить это поле (метод clear())
# 5. Ввести в поле текст "Pro"
# 6. Закрыть браузер (метод quit())

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def input_field_operations():
    
    print("Запуск скрипта для работы с полем ввода")
        
#1. Открыть браузер Firefox
    print("\n1. Запуск браузера Firefox")
    driver = webdriver.Firefox()
    
    try:
#2. Перейти на страницу: http://the-internet.herokuapp.com/inputs
        print("2. Переход на страницу http://the-internet.herokuapp.com/inputs")
        driver.get("http://the-internet.herokuapp.com/inputs")
        
        #Создаем объект для явных ожиданий (максимум 10 секунд)
        wait = WebDriverWait(driver, 10)
        
        #Ждем загрузки страницы
        print("   Ожидание загрузки страницы")
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        
        #На этой странице поле ввода имеет тип "number"
        print("3. Поиск поля ввода")
        input_field = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
        
        #Проверяем атрибуты поля
        input_type = input_field.get_attribute("type")
        print(f"   Найдено поле ввода типа: '{input_type}'")
        
#3. Ввести в поле текст "Sky"
        print("4. Ввод текста 'Sky' в поле")
        input_field.send_keys("Sky")
        
        #Проверяем, что текст введен
        current_value = input_field.get_attribute("value")
        print(f"   Текущее значение поля: '{current_value}'")
        
        sleep(2)
        
#4. Очистить это поле (метод clear())
        print("5. Очистка поля ввода")
        input_field.clear()
        
        #Проверяем, что поле очищено
        current_value = input_field.get_attribute("value")
        print(f"   Значение после очистки: '{current_value}'")
        
        sleep(1)
        
#5. Ввести в поле текст "Pro"
        print("6. Ввод текста 'Pro' в поле")
        input_field.send_keys("Pro")
        
        #Проверяем результат
        current_value = input_field.get_attribute("value")
        print(f"   Финальное значение поля: '{current_value}'")
        
        sleep(2)
        
        print("\n Все операции выполнены успешно!")
        
    except Exception as e:
        print(f"\n Произошла ошибка: {e}")
        
        #Делаем скриншот при ошибке для отладки
        try:
            driver.save_screenshot("error_input_field.png")
            print("   Скриншот ошибки сохранен как 'error_input_field.png'")
        except:
            pass
        
    finally:
#6. Закрыть браузер (метод quit())
        print("\n7. Закрытие браузера")
        driver.quit()
        print("   Браузер успешно закрыт.")


if __name__ == "__main__":
   input_field_operations()   
   