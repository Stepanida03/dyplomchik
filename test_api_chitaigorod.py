import allure
import pytest
from .api_chitaigorod import ChitaiGorodAPI
from .config import API_URL


url = ChitaiGorodAPI(API_URL)


@allure.feature("API проверки веб-сайта'Читай город'")
@allure.severity("critical")
@pytest.mark.api_test
@pytest.mark.parametrize("title", [
    "Мастер и Маргарита"
])
def test_search_book_name_positive(title: str):
    with allure.step("Поиск по названию"):
        result = url.search_product(phrase=title)
        assert result.status_code == 200
        

@allure.feature("API проверки веб-сайта'Читай город'")
@allure.severity("critical")
@pytest.mark.api_test
@pytest.mark.parametrize("title", [
    "Булгаков"
])
def test_search_book_author_positive(title: str):
    with allure.step("Поиск по автору"):
        result = url.search_product(phrase=title)
        assert result.status_code == 200       


@allure.feature("API проверки веб-сайта'Читай город'")
@allure.severity("critical")
@pytest.mark.api_test
@pytest.mark.parametrize("title", [
    "Рассказы"
])
def test_search_book_genre_positive(title: str):
    with allure.step("Поиск по жанру"):
        result = url.search_product(phrase=title)
        assert result.status_code == 200        


@allure.feature("API проверки веб-сайта'Читай город'")
@allure.severity("critical")
@pytest.mark.api_test
@pytest.mark.parametrize("title", [
    "№*&"
])
def test_search_book_name_negative(title: str):
    with allure.step("Спецсимволы в поисковой строке"):
        result = url.search_product(phrase=title)
        assert result.status_code == 422
        assert result.json()['errors'][0]
        ['title'] == "Недопустимая поисковая фраза"
       

@allure.feature("API проверки веб-сайта'Читай город'")
@allure.severity("critical")
@pytest.mark.api_test
@pytest.mark.parametrize("title", [
    " "
])
def test_search_book_empty_field_negative(title: str):
    with allure.step("Пустая поисковая строка"):
        result = url.search_product(phrase=title)
        assert result.status_code == 400
        assert result.json()['errors'][0]
        ['title'] == "Phrase должен содержать минимум 2 символа"
