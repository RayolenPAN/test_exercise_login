from pages.base_pages import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = "input[data-test='username']"
    PASSWORD_INPUT = "input[data-test='password']"
    LOGIN_BUTTON = "input[data-test='login-button']"
    ERROR_MESSAGE = "h3[data-test='error']"

    def __init__(self, page: BasePage):
        super().__init__(page)
        self.base_url = "https://www.saucedemo.com/"
    def open_page(self):
        self.page.goto(self.base_url)
    def login(self, username: str, password: str):
        self.wait_for_element(self.USERNAME_INPUT).fill(username)
        self.wait_for_element(self.PASSWORD_INPUT).fill(password)
        self.wait_for_element(self.LOGIN_BUTTON).click()
    def error(self) ->str:
        if self.is_element_visible(self.ERROR_MESSAGE):
            return self.page.inner_text(self.ERROR_MESSAGE)
        return ""
    def click_login(self):
        self.wait_for_element(self.LOGIN_BUTTON).click()

