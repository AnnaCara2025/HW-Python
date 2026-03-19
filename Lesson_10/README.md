# Проект автоматизации тестирования

Данный проект содержит автоматические тесты для двух веб-приложений:
- **Медленный калькулятор** (https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html)
- **Интернет-магазин Saucedemo** (https://www.saucedemo.com/)

Тесты написаны на Python с использованием **Selenium WebDriver**, **Pytest** и **Allure Framework** для отчётности.

---

## Базовый синтаксис и форматирование кода

### Page Objects
- Каждая страница представлена отдельным классом в соответствующем модуле.
- Локаторы элементов хранятся как константы класса (кортежи `(By, value)`).
- Методы страниц выполняют конкретные действия (клик, ввод текста, получение данных) и используют `WebDriverWait` для ожидания элементов.
- Все методы документируются с помощью docstring, где указаны типы параметров и возвращаемых значений.
- Для улучшения читаемости добавлены **аннотации типов** (type hints).

### Allure
- Для каждого значимого действия в Page Object используется декоратор `@allure.step` с описанием шага.
- В тестовых функциях логические блоки оборачиваются в контекстный менеджер `with allure.step("..."):`.
- Проверки (assert) также выделяются в отдельные шаги.
- Тесты снабжены декораторами Allure:
  - `@allure.feature` — функциональность (например, "Calculator", "Shop").
  - `@allure.severity` — критичность (blocker, critical, normal и т.д.).
  - `@allure.title` — заголовок теста (может включать параметры).
  - `@allure.description` — подробное описание теста.

### Пример оформления теста
```python
@allure.feature("Calculator")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Сложение двух чисел")
@allure.description("Проверка базовой операции сложения.")
def test_addition(driver):
    with allure.step("Открыть страницу"):
        page.open()
    with allure.step("Выполнить вычисления"):
        page.click_button("2")
        page.click_button("+")
        page.click_button("3")
        page.click_button("=")
    with allure.step("Проверить результат"):
        assert page.get_result() == "5"
