# Задание:
# 1. Открыть браузер Firefox
# 2. Перейти на страницу http://the-internet.herokuapp.com/login
# 3. В поле username ввести значение tomsmith
# 4. В поле password ввести значение SuperSecretPassword!
# 5. Нажать кнопку Login
# 6. Вывести текст с зеленой плашки в консоль
# 7. Закрыть браузер (метод quit())

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def login_form_operations():
    print("СКРИПТ АВТОРИЗАЦИИ НА ТЕСТОВОЙ СТРАНИЦЕ")
    
#1. Открыть браузер Firefox
    print("\n1. Запуск браузера Firefox")
    driver = webdriver.Firefox()
    
    try:
#2. Перейти на страницу http://the-internet.herokuapp.com/login
        print("\n2. Переход на страницу авторизации")
        print("   URL: http://the-internet.herokuapp.com/login")
        driver.get("http://the-internet.herokuapp.com/login")
        
        #Создаем объект для явных ожиданий (максимум 10 секунд)
        wait = WebDriverWait(driver, 10)
        
        #Ждем загрузки страницы
        print("   Ожидание загрузки страницы")
        wait.until(EC.presence_of_element_located((By.ID, "login")))
        
#3. В поле username ввести значение tomsmith
        print("\n3. Заполнение поля username")
        username_field = driver.find_element(By.ID, "username")
        username_field.clear()
        username_field.send_keys("tomsmith")
        print("   Введен username: tomsmith")
        
#4. В поле password ввести значение SuperSecretPassword!
        print("\n4. Заполнение поля password")
        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys("SuperSecretPassword!")
        print("   Введен password: SuperSecretPassword!")
        
        sleep(1)
        
#5. Нажать кнопку Login
        print("\n5. Нажатие кнопки Login")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        print("   Кнопка Login нажата")
        
        #Ждем загрузки страницы после авторизации
        print("   Ожидание завершения авторизации")
        sleep(2)
        
#6. Вывести текст с зеленой плашки в консоль
        print("\n6. Получение текста из зеленой плашки")
        
        #Ищем элемент с сообщением об успехе (зеленая плашка)
        try:
            #Способ 1: Поиск по классу флэш-сообщения
            flash_message = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "flash"))
            )
            
            #Проверяем, что это успешное сообщение (зеленое)
            flash_classes = flash_message.get_attribute("class")
            
            if "success" in flash_classes:
                #Получаем чистый текст без закрывающего крестика
                flash_text = flash_message.text.strip()
                
                #Убираем текст крестика (×) если он есть
                if "×" in flash_text:
                    flash_text = flash_text.split("×")[1].strip()
                
                print("   🟢 ТЕКСТ ЗЕЛЕНОЙ ПЛАШКИ:")
                print(f"   {flash_text}")
                
                #Также выводим дополнительную информацию
                print(f"\n   Дополнительная информация:")
                print(f"   - Классы элемента: {flash_classes}")
                print(f"   - Полный текст: '{flash_message.text}'")
            else:
                print("   Найден flash-элемент, но это не зеленая плашка")
                print(f"   Классы элемента: {flash_classes}")
                
        except Exception as flash_error:
            print(f"   Ошибка при поиске зеленой плашки: {flash_error}")
            
            #Альтернативный способ поиска
            try:
                flash_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")
                flash_text = flash_message.text.strip()
                if "×" in flash_text:
                    flash_text = flash_text.split("×")[1].strip()
                print("   🟢 ТЕКСТ ЗЕЛЕНОЙ ПЛАШКИ (альтернативный поиск):")
                print(f"   {flash_text}")
            except:
                print("   ❌ Не удалось найти зеленую плашку")
        
        #Делаем скриншот успешной авторизации
        try:
            driver.save_screenshot("login_success.png")
            print("\n   Скриншот страницы сохранен как 'login_success.png'")
        except:
            pass
        
        #Небольшая пауза для визуальной проверки
        print("\n7. Краткая пауза для визуальной проверки")
        sleep(3)
        
        print("   АВТОРИЗАЦИЯ УСПЕШНО ЗАВЕРШЕНА")
        
    except Exception as e:
        print(f"\n ПРОИЗОШЛА ОШИБКА: {e}")
        
        #Делаем скриншот при ошибке для отладки
        try:
            driver.save_screenshot("login_error.png")
            print("   Скриншот ошибки сохранен как 'login_error.png'")
        except:
            pass
        
        #Показываем текущий URL для отладки
        print(f"   Текущий URL: {driver.current_url}")
        
    finally:
#7. Закрыть браузер (метод quit())
        print("\n8. Закрытие браузера")
        driver.quit()
        print("   Браузер успешно закрыт.")


if __name__ == "__main__":
    login_form_operations()
   
