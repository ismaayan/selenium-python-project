from selenium.webdriver.common.by import By
from pages.BasePage import BasePage



class ItemPage(BasePage):
    quantity_input = (By.NAME, "quantity")
    add_to_cart_button = (By.NAME, "add-to-cart")


    def update_album_item_quantity_and_add_to_cart(self, quantity):
        self.clear_text(self.quantity_input)
        self.do_send_keys(self.quantity_input, quantity)

        # Add the item to the cart
        self.do_click(self.add_to_cart_button)