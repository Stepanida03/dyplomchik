import allure
import pytest
from .api_chitaigorod import ChitaiGorodAPI
from .config import API_URL


url = ChitaiGorodAPI(API_URL)


@allure.feature("API проверки веб-сайта'Читай город'")
@allure.severity("critical")
@pytest.mark.api_test
@pytest.mark.parametrize("title", [
    "маугли",
    "педагогическая поэма"
])
def test_search_book_name_positive(title: str):
    with allure.step("Ввести название на кирилие"):
        result = url.search_product(phrase=title)
        assert result.status_code == 200
        assert result.json()["data"]["attributes"]
        ["transformedPhrase"] == title


@allure.feature("API проверки веб-сайта'Читай город'")
@allure.severity("critical")
@pytest.mark.api_test
@pytest.mark.parametrize("title", [
    "首教学诗",
    "😀😀😀"
])
def test_search_book_name_negative(title: str):
    with allure.step("Ввести название невалидными значениями"):
        result = url.search_product(phrase=title)
        assert result.status_code == 422
        assert result.json()['errors'][0]
        ['title'] == "Недопустимая поисковая фраза"


@allure.feature("API проверки веб-сайта'Читай город'")
@allure.severity("critical")
@pytest.mark.api_test
@pytest.mark.parametrize("title", [
    "киплинг",
    "макаренко"
])
def test_search_book_author_positive(title: str):
    with allure.step("Ввести автора"):
        result = url.search_product(phrase=title)
        assert result.status_code == 200
        assert result.json()["data"]["attributes"]
        ["transformedPhrase"] == title


@allure.feature("API проверки веб-сайта'Читай город'")
@allure.severity("critical")
@pytest.mark.api_test
@pytest.mark.parametrize("title", [
    "художественная литература",
    "комиксы"
])
def test_search_book_genre_positive(title: str):
    with allure.step("Ввести нужный критерий отбора"):
        result = url.search_product(phrase=title)
        assert result.status_code == 200
        assert result.json()["data"]["attributes"]
        ["transformedPhrase"] == title


@allure.feature("API проверки веб-сайта'Читай город'")
@allure.severity("critical")
@pytest.mark.api_test
@pytest.mark.parametrize("title", [
    " "
])
def test_search_book_empty_field_negative(title: str):
    with allure.step("Оставить поле ввода пустое"):
        result = url.search_product(phrase=title)
        assert result.status_code == 400
        assert result.json()['errors'][0]
        ['title'] == "Phrase должен содержать минимум 2 символа"
