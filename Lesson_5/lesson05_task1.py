# Задание:
# 1. Открыть браузер Google Chrome
# 2. Перейти на страницу: http://uitestingplayground.com/classattr
# 3. Кликнуть на синюю кнопку
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
  
def click_blue_button():
 
#1. Открыть браузер Google Chrome
    print("Запуск браузера Chrome")
    driver = webdriver.Chrome()
    
    try:
#2. Перейти на страницу: http://uitestingplayground.com/classattr
        print("Переход на страницу http://uitestingplayground.com/classattr")
        driver.get("http://uitestingplayground.com/classattr")
        
        #Создаем объект для явных ожиданий (максимум 10 секунд)
        wait = WebDriverWait(driver, 10)
        
#3. Кликнуть на синюю кнопку
        #Используем XPath из описания на странице
        blue_button_xpath = "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"
        
        print("Поиск синей кнопки")
        blue_button = wait.until(EC.element_to_be_clickable((By.XPATH, blue_button_xpath)))
        
        #Выводим информацию о найденной кнопке для отладки
        print(f"Найдена кнопка: текст='{blue_button.text}', "f"классы='{blue_button.get_attribute('class')}'")
        
        #Кликаем по кнопке
        print("Кликаем по синей кнопке")
        blue_button.click()
        
        #Обработка всплывающего окна (alert)
        try:
            #Даем время для появления alert
            sleep(2)
            
            #Переключаемся на alert
            alert = driver.switch_to.alert
            print(f"Обнаружено всплывающее окно с текстом: '{alert.text}'")
            
            #Нажимаем OK в alert
            alert.accept()
            print("Нажата кнопка OK во всплывающем окне")
        except:
            #Если alert не появился, продолжаем выполнение
            print("Всплывающее окно не обнаружено")
        
        #Небольшая пауза для визуальной проверки
        sleep(2)
        print("Действие успешно выполнено!")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        
    finally:
        print("Закрытие браузера")
        driver.quit()


if __name__ == "__main__": 
#Скрипт нужно запускать вручную три раза подряд.
    click_blue_button()
