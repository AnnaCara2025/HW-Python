import os
import pytest
import requests
import uuid

BASE_URL = "https://yougile.com"
API_KEY = "ВАШ_РЕАЛЬНЫЙ_КЛЮЧ"  # замените на свой ключ

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def generate_unique_title():
    """Генерирует уникальное название проекта для избежания конфликтов."""
    return f"Test Project {uuid.uuid4()}"


# Фикстура, которая создаёт проект и гарантированно удаляет его после теста
@pytest.fixture
def created_project():
    title = generate_unique_title()
    response = requests.post(
        f"{BASE_URL}/api-v2/projects",
        headers=HEADERS,
        json={"title": title}
    )
    # Проверяем, что проект создан успешно
    assert response.status_code == 201, f"Не удалось создать проект: {response.text}"
    project_id = response.json()["id"]
    yield project_id  # передаём ID в тест

    # После завершения теста удаляем проект
    delete_response = requests.delete(f"{BASE_URL}/api-v2/projects/{project_id}", headers=HEADERS)
    if delete_response.status_code not in (200, 204):
        print(f"Предупреждение: не удалось удалить проект {project_id}, код {delete_response.status_code}")


# Тест на создание проекта (использует фикстуру, чтобы не плодить проекты)
def test_create_project_positive(created_project):
    """Позитивный тест: создание проекта с корректным телом."""
    # Здесь project_id уже создан фикстурой, но мы можем его использовать для проверок
    project_id = created_project
    # Дополнительно можно проверить, что проект действительно существует
    # Например, получить его по ID
    get_response = requests.get(f"{BASE_URL}/api-v2/projects/{project_id}", headers=HEADERS)
    assert get_response.status_code == 200, "Созданный проект не найден"
    data = get_response.json()
    assert "id" in data, "Ответ не содержит id проекта"

def test_create_project_negative_empty_body():
    """Негативный тест: создание проекта с пустым телом (ожидается 400)."""
    response = requests.post(
        f"{BASE_URL}/api-v2/projects",
        headers=HEADERS,
        json={}  # пустое тело
    )
    assert response.status_code == 400, f"Ожидался код 400, получен {response.status_code}"


# 2. Тесты на изменение проекта
def test_update_project_positive(created_project):
    """Позитивный тест: изменение названия существующего проекта."""
    project_id = created_project
    new_title = f"Updated {generate_unique_title()}"
    response = requests.put(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        headers=HEADERS,
        json={"title": new_title}
    )
    assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
    # Проверим, что изменения применились, выполнив GET
    get_response = requests.get(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        headers=HEADERS
    )
    assert get_response.status_code == 200
    assert get_response.json()["title"] == new_title, "Название не обновилось"


def test_update_project_negative_no_id():
    """Негативный тест: PUT запрос без указания ID (ожидается 404 или 405)."""
    new_title = generate_unique_title()
    response = requests.put(
        f"{BASE_URL}/api-v2/projects/",  # без ID
        headers=HEADERS,
        json={"title": new_title}
    )
    assert response.status_code in (404, 405), f"Ожидался 404 или 405, получен {response.status_code}"


# 3. Тесты на получение проекта по ID
def test_get_project_by_id_positive(created_project):
    """Позитивный тест: получение проекта по ID с авторизацией."""
    project_id = created_project
    response = requests.get(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        headers=HEADERS
    )
    assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
    data = response.json()
    assert data["id"] == project_id, "ID проекта не совпадает"
    assert "title" in data, "Ответ не содержит названия"


def test_get_project_by_id_negative_no_auth(created_project):
    """Негативный тест: получение проекта без авторизации (ожидается 401)."""
    project_id = created_project
    response = requests.get(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        headers={}  # без токена
    )
    assert response.status_code == 401, f"Ожидался код 401, получен {response.status_code}"
