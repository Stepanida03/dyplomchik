from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .config import UI_URL


class ChitaiGorodUI:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def delay_driver(self):
        """
           Пауза
        """
        self.driver.implicitly_wait(5)

    def open_main_page(self):
        """
           Зайти на сайт
        """
        self.driver.get(UI_URL)

    def get_page_text(self):
        """
           Получить заглавие страницы
        """
        return self.driver.title

    def logo(self):
        """
           Логотип сайта
        """
        logo = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "svg.header__logo"))
            )
        return logo.is_displayed()

    def resize_browser(self, width: int, height: int):
        """
           Задать размеры экрана
        """
        self.driver.set_window_size(width, height)

    def maximize_browser(self):
        """
           Максимальный размер экрана
        """
        self.driver.maximize_window()

    def search_product(self, name: str):
        """
           Ввод названия товара
           Нажать на иконку Поиск
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "input[name='search']"
            ).send_keys(name)
        self.driver.find_element(
            By.CSS_SELECTOR, "button[aria-label='Найти']"
            ).click()
        return self.driver.title

    def click_basket(self):
        """
           Зайти в корзину
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[aria-label='Корзина']")
                )
            ).click()

    def page_name_basket(self):
        """
           Получить название страницы
        """
        txt = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "h1.cart-page__title"))
                ).text
        return (txt)

    def button_auth(self):
        """
           Кнопка Входа и Авторизации
        """
        self.driver.find_element(
            By.CSS_SELECTOR, ".header-controls__btn[aria-label='Меню профиля']"
            ).click()

    def get_field_name(self):
        """
           Проверить текст открывшегося окна
        """
        txt = self.driver.find_element(
            By.CSS_SELECTOR, "div.ui-header-modal__title"
            ).text
        return (txt)

    def close_browser(self):
        """
           Закрыть браузер
        """
        self.driver.quit()

    def search_title(self):
        """
        Результаты поиска
        """
        txt = self.driver.find_element(
            By.CSS_SELECTOR, "#__nuxt > div > div.app-wrapper__content > div > div > h1"
            ).text
        return (txt)
    
    def cart_page__clear_cart_title(self):
        """
           Очистить корзину
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#__nuxt > div > div.app-wrapper__content > div > div > div > div.cart-page__head > div > div.cart-page__delete-many > span")
                )
            ).click()

    def chg_app_button__content(self):
        """
           Восстановить корзину
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#__nuxt > div > div.app-wrapper__content > div > div > div > section > div > button.chg-app-button.chg-app-button--primary.chg-app-button--s.chg-app-button--brand-blue.cart-multiple-delete__button.cart-multiple-delete__button > div")
                )
            ).click()
