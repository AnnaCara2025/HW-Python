# 1. Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html в Edge.
# 2. Заполните форму значениями:
# 3. Нажмите кнопку Submit. 
# 4. Проверьте (assert), что поле Zip code подсвечено красным.
# 5. Поверьте (assert), что остальные поля подсвечены зеленым.


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    """Фикстура для инициализации и закрытия браузера Edge"""
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_validation(browser):
    """Тест проверки валидации формы"""
    
    # 1. Открываем страницу
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    wait = WebDriverWait(browser, 10)
    
    # 2. Заполняем форму
    # Ждем загрузки формы
    form = wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
    
    # First name
    first_name = browser.find_element(By.CSS_SELECTOR, "input[name='first-name']")
    first_name.send_keys("Иван")
    
    # Last name
    last_name = browser.find_element(By.CSS_SELECTOR, "input[name='last-name']")
    last_name.send_keys("Петров")
    
    # Address
    address = browser.find_element(By.CSS_SELECTOR, "input[name='address']")
    address.send_keys("Ленина, 55-3")
    
    # Email
    email = browser.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
    email.send_keys("test@skypro.com")
    
    # Phone number
    phone = browser.find_element(By.CSS_SELECTOR, "input[name='phone']")
    phone.send_keys("+7985899998787")
    
    # Zip code - оставляем пустым (не заполняем)
    
    # City
    city = browser.find_element(By.CSS_SELECTOR, "input[name='city']")
    city.send_keys("Москва")
    
    # Country
    country = browser.find_element(By.CSS_SELECTOR, "input[name='country']")
    country.send_keys("Россия")
    
    # Job position
    job_position = browser.find_element(By.CSS_SELECTOR, "input[name='job-position']")
    job_position.send_keys("QA")
    
    # Company
    company = browser.find_element(By.CSS_SELECTOR, "input[name='company']")
    company.send_keys("SkyPro")
    
    # 3. Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
    # 4. Проверяем, что поле Zip code подсвечено красным
    # Ждем применения стилей валидации к полю Zip code
    zip_code_field = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[class='alert py-2 alert-danger']"))
    )
    zip_code_classes = zip_code_field.get_attribute("class")
    assert "alert py-2 alert-danger" in zip_code_classes, "Поле Zip code должно быть подсвечено красным"
    
    # 5. Проверяем, что остальные поля подсвечены зеленым
    valid_fields = [
        "first-name",
        "last-name", 
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]
    
    for field_name in valid_fields:
        # Для каждого поля ждем появления класса is-valid
        field_locator = (By.ID, f"{field_name}")
        
        try:
            # Пытаемся найти поле с классом is-valid
            field = wait.until(EC.presence_of_element_located(field_locator))
        except:
            # Если не нашли с классом is-valid, ищем поле без класса
            field = browser.find_element(By.ID, f"{field_name}")
            field_classes = field.get_attribute("class")
            raise AssertionError(
                f"Поле {field_name} должно быть подсвечено зеленым, "
                f"но имеет классы: {field_classes}"
            )
        
        # Проверяем, что поле действительно имеет класс is-valid
        field_classes = field.get_attribute("class")
        assert "alert py-2 alert-success" in field_classes, f"Поле {field_name} должно быть подсвечено зеленым"

