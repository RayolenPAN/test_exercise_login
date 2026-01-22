import allure
import pytest
from playwright.sync_api import expect


@allure.epic("Авторизация")
class TestLoginPage:
    @allure.title("Тест 1: Успешный логин")
    def test_successful_login(self, login_page, inventory_page):
        with allure.step("Ввести логин и пароль"):
            login_page.login("standard_user", "secret_sauce")
        with allure.step("Проверка успешного входа"):
            expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")
            assert inventory_page.check_display()
            title = inventory_page.get_page_title()
            assert title == "Products", f"Ожидался заголовок 'Products', получен: '{title}'"



    @allure.title("Тест 2: Логин с неверным паролем")
    def test_login_wrong_password(self, login_page):
        with allure.step("Ввести логин и пароль"):
            login_page.login("standard_user", "00000000")
        with allure.step("Проверка появления ошибки при неверном пароле"):
            error_text = login_page.error()
            assert "Username and password do not match" in error_text, f"Вместо ошибки получено: {error_text}"
    @allure.title("Тест 3: Логин заблокированного пользователя")
    def test_login_locked_user(self, login_page):
        with allure.step("Ввести логин и пароль"):
            login_page.login("locked_out_user", "secret_sauce")
        with allure.step("Проверка появления ошибки заблокированного пользователя"):
            error_text = login_page.error()
            assert "Sorry, this user has been locked out." in error_text,f"Вместо ошибки получено: {error_text}"

    @allure.title("Тест 4: Логин с пустыми полями")
    def test_login_with_empty_fields(self, login_page):
        with allure.step("Ввести логин и пароль"):
            login_page.click_login()
        with allure.step("Проверка появления ошибки при вводе пустых полей"):
            error_text = login_page.error()
            assert "Username is required" in error_text, f"Вместо ошибки получено: {error_text}"

    @allure.title("Тест 5: Логин пользователем performance_glitch_user")
    def test_glitch_login(self, login_page, inventory_page):
        with allure.step("Ввести логин и пароль"):
            login_page.login("performance_glitch_user", "secret_sauce")
        with allure.step("Проверка успешного входа с задержкой"):
            expect(inventory_page.page.locator(inventory_page.PRODUCTS_CONTAINER)).to_be_visible(timeout=15000)
            assert "inventory" in inventory_page.get_current_url(),"Не произошел переход на страницу товаров"