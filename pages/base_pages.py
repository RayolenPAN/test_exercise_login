from playwright.sync_api import Page

class BasePage():
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 10000
    def go_to(self, url: str):
        self.page.goto(url)
    def get_current_url(self):
        return self.page.url

    def wait_for_element(self, locator: str, timeout: int = None):
        timeout = timeout or self.timeout
        return self.page.wait_for_selector(locator, timeout=timeout)
    def is_element_visible(self, locator: str) -> bool:
        return self.page.is_visible(locator)
    #функция для скриншота в allure