import pytest
from playwright.sync_api import Page, Browser

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page:Page) -> LoginPage:
    login_page=LoginPage(page)
    login_page.open_page()
    return login_page
@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    return InventoryPage(page)