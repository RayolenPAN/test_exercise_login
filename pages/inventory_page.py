from pages.base_pages import BasePage


class InventoryPage(BasePage):
    PRODUCTS_CONTAINER = "div.inventory_container"
    SHOPPING_CART = "a.shopping_cart_link"
    TITLE = "span.title"
    def __init__(self, page):
        super().__init__(page)

    def check_display(self):
        try:
            self.wait_for_element(self.PRODUCTS_CONTAINER)
            return True
        except:
            return False
    def get_page_title(self) -> str:
        return self.wait_for_element(self.TITLE).inner_text()

    def get_current_url(self) -> str:
        return super().get_current_url()


