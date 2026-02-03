import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# Тесты для capitalize()
@pytest.mark.positive
@pytest.mark.capitalize
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("a", "A"),
    ("alREADY", "AlREADY")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.capitalize
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("ALREADY", "ALREADY"),  # Важно: capitalize делает только первую букву заглавной
    ("!test", "!test"),
    (" skypro", " skypro")  # Пробел в начале
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# Тесты для trim()
@pytest.mark.positive
@pytest.mark.trim
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello  ", "hello  "),
    (" ", ""),
    ("    a", "a"),
    ("", ""),
    ("   test", "test")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.trim
@pytest.mark.parametrize("input_str, expected", [
    ("\nskypro", "\nskypro"),  # Перенос строки не удаляется
    ("skypro   ", "skypro   "),  # Пробелы в конце не удаляются
    ("\t  test", "\t  test"),  # Табы не удаляются
    ("  \n  test", "  \n  test")  # Переносы не удаляются
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# Тесты для contains()
@pytest.mark.positive
@pytest.mark.contains
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("SkyPro", "Pro", True),
    ("Hello World", " ", True),
    ("123", "2", True),
    ("", "", True),  # Особый случай: пустая строка содержит пустую подстроку
    ("test", "", True)  # Любая строка содержит пустую подстроку
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.contains
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),
    ("test", "TEST", False),  # Регистрозависимость
    ("abc", "abcd", False),  # Подстрока длиннее строки
    ("   ", "a", False),  # Пробелы
    ("hello", "x", False)
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

# Тесты для delete_symbol()
@pytest.mark.positive
@pytest.mark.delete_symbol
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("Hello World", " ", "HelloWorld"),
    ("aaaa", "a", ""),
    ("ababab", "ab", ""),
    ("test", "x", "test"),  # Символ не найден - строка без изменений
    ("banana", "na", "ba"),
    ("mississippi", "si", "missippi")
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.delete_symbol
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "a", ""),  # Пустая строка
    ("aaa", "", "aaa"),  # Пустая подстрока - должна вернуть оригинал
    ("   ", " ", ""),  # Удаление пробелов
    ("abc", "abc", ""),  # Удаление всей строки
    ("test!test", "!", "testtest"),  # Удаление спецсимвола
    ("abca", "a", "bc"),  # Удаление первого и последнего символа
    ("", "", ""),  # Две пустые строки
    ("abc", "d", "abc")  # Символ не найден
])
def test_delete_symbol_edge_cases(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

