# Задание:
# 1. Открыть браузер Google Chrome
# 2. Перейти на страницу: http://uitestingplayground.com/dynamicid
# 3. Кликнуть на синюю кнопку (кнопка с динамически изменяющимся ID)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def click_button_without_id():
  
#1. Открыть браузер Google Chrome
    print("Запуск браузера Chrome")
    driver = webdriver.Chrome()
    
    try:
#2. Перейти на страницу: http://uitestingplayground.com/dynamicid
        print("Переход на страницу http://uitestingplayground.com/dynamicid")
        driver.get("http://uitestingplayground.com/dynamicid")
        
        #Создаем объект для явных ожиданий (максимум 10 секунд)
        wait = WebDriverWait(driver, 10)
        
#3. Кликнуть на синюю кнопку
        print("Поиск синей кнопки")
        
        #Способ_1: Поиск по классу кнопки (наиболее надежный)
        try:
            #Кнопка имеет класс 'btn-primary'
            blue_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))
            )
            print("Кнопка найдена по классу 'btn-primary'")
            
        except:
        #Способ_2: Поиск по тексту кнопки
            blue_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Button with Dynamic ID']"))
            )
            print("Кнопка найдена по тексту 'Button with Dynamic ID'")
        
        #Выводим информацию о найденной кнопке для отладки
        button_id = blue_button.get_attribute("id")
        button_class = blue_button.get_attribute("class")
        button_text = blue_button.text
        
        print(f"Найдена кнопка: ID='{button_id}', "
              f"класс='{button_class}', "
              f"текст='{button_text}'")
        
        #Выводим предупреждение, если ID меняется при обновлении страницы
        if button_id and "dynamic" in button_id.lower():
            print(f"Внимание: Кнопка имеет динамический ID ({button_id})")
        
        #Кликаем по кнопке
        print("Кликаем по синей кнопке")
        blue_button.click()
        
        print("Клик выполнен успешно!")
        
        sleep(3)
        print("Успешно выполнено!")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        #Делаем скриншот при ошибке для отладки
        try:
            driver.save_screenshot("error_SC.png")
            print("Скриншот ошибки сохранен как 'error_SC.png'")
        except:
            pass
        
    finally:
        print("Закрытие браузера")
        driver.quit()


if __name__ == "__main__":
    print("=" * 50)
    print("Запуск скрипта для клика по кнопке без статического ID")
    print("=" * 50)
    
    click_button_without_id()
 
