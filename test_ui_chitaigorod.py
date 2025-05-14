import pytest
import allure
from .ui_chitaigorod import ChitaiGorodUI


@allure.feature("UI проверки веб-сайта'Читай город'")
@allure.title("Название сайта")
@allure.severity("critical")
@pytest.mark.ui_test
def test_chitai_gorod_title_size():
    with allure.step("Открыть браузер"):
        main_page = ChitaiGorodUI()
    with allure.step("Свернуть окно согласно заданным размерам"):
        main_page.resize_browser(100, 700)
    with allure.step("Зайти на сайт"):
        main_page.open_main_page()
    with allure.step("Проверить текст страницы"):
        assert main_page.get_page_text() ==\
            '«Читай-город» – интернет-магазин книг'
    with allure.step("Закрыть браузер"):
        main_page.close_browser()


@allure.feature("UI проверки веб-сайта'Читай город'")
@allure.title("Название сайта")
@allure.severity("critical")
@pytest.mark.ui_test
def test_chitai_gorod_title_max():
    with allure.step("Открыть браузер"):
        main_page = ChitaiGorodUI()
    with allure.step("Развернуть окно"):
        main_page.maximize_browser()
    with allure.step("Зайти на сайт"):
        main_page.open_main_page()
    with allure.step("Проверить текст страницы"):
        assert main_page.get_page_text() ==\
                '«Читай-город» – интернет-магазин книг'
    with allure.step("Закрыть браузер"):
        main_page.close_browser()


@allure.feature("UI проверки веб-сайта'Читай город'")
@allure.title("Поиск")
@allure.severity("critical")
@pytest.mark.ui_test
def test_shopping_items():
    with allure.step("Открыть браузер"):
        main_page = ChitaiGorodUI()
    with allure.step("Развернуть окно"):
        main_page.maximize_browser()
    with allure.step("Зайти на сайт"):
        main_page.open_main_page()
    with allure.step("Ввести текст в поле поиска, кликнуть кнопку Найти"):
        main_page.search_product("Педагогическая поэма")
    with allure.step("Подождать"):
        main_page.delay_driver()
    with allure.step("Появился список товаров"):
        expected_title = "Результаты поиска"
        assert main_page.search_product("Результаты поиска") == expected_title
    with allure.step("Закрыть браузер"):
        main_page.close_browser()


@allure.feature("UI проверки веб-сайта'Читай город'")
@allure.title("Корзина")
@allure.severity("critical")
@pytest.mark.ui_test
def test_go_to_cart():
    with allure.step("Открыть браузер"):
        main_page = ChitaiGorodUI()
    with allure.step("Развернуть окно"):
        main_page.maximize_browser()
    with allure.step("Зайти на сайт"):
        main_page.open_main_page()
    with allure.step("Кликнуть на кнопку Корзина"):
        main_page.click_basket()
    with allure.step("Проверить текст"):
        txt = main_page.page_name_basket()
        assert (txt) == "КОРЗИНА"
    with allure.step("Закрыть браузер"):
        main_page.close_browser()


@allure.feature("UI проверки веб-сайта'Читай город'")
@allure.title("Авторизация")
@allure.severity("critical")
@pytest.mark.ui_test
def test_auth():
    with allure.step("Открыть браузер"):
        main_page = ChitaiGorodUI()
    with allure.step("Развернуть окно"):
        main_page.maximize_browser()
    with allure.step("Зайти на сайт"):
        main_page.open_main_page()
    with allure.step("Кликнуть на кнопку авторизации"):
        main_page.button_auth()
        txt = main_page.get_field_name()
    with allure.step("Подождать"):
        main_page.delay_driver()
    with allure.step("Проверить текст"):
        assert (txt) == "Вход и регистрация"
    with allure.step("Закрыть браузер"):
        main_page.close_browser()


@allure.feature("UI проверки веб-сайта'Читай город'")
@allure.title("Логотип")
@allure.severity("critical")
@pytest.mark.ui_test
def test_chitai_gorod_logo():
    with allure.step("Открыть браузер"):
        main_page = ChitaiGorodUI()
    with allure.step("Свернуть окно согласно заданным размерам"):
        main_page.resize_browser(100, 700)
    with allure.step("Зайти на сайт"):
        main_page.open_main_page()
    with allure.step("Проверить наличие логотипа"):
        assert main_page.logo() is True
    with allure.step("Закрыть браузер"):
        main_page.close_browser()
