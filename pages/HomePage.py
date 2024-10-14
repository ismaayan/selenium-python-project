import time
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class HomePage(BasePage):

    first_add_button = (By.CLASS_NAME, 'add_to_cart_button')
    album_item = (By.CSS_SELECTOR, "li.post-24 bdi:nth-child(1)")
    beanie_item = (By.CSS_SELECTOR, "li.post-16 ins bdi:nth-child(1)")
    beanie_with_logo_item = (By.CSS_SELECTOR, "li.post-33 ins bdi:nth-child(1)")
    belt_item = (By.CSS_SELECTOR, "li.post-17 ins bdi:nth-child(1)")
    add_album_item = (By.XPATH, "//a[@aria-label='Add “Album” to your cart']")
    add_beanie_item = (By.XPATH, "//a[@aria-label='Add “Beanie” to your cart']")
    add_beanie_with_logo_item = (By.XPATH, "//a[@aria-label='Add “Beanie with Logo” to your cart']")
    add_belt_item = (By.XPATH, "//a[@aria-label='Add “Belt” to your cart']")

    def __init__(self, driver):
        super().__init__(driver)
        self.items_total_price = None

    def shop_item_count(self):
        shop_items = self.driver.find_elements(By.CSS_SELECTOR, "#main ul li.product")
        assert len(shop_items) == 16, f"Expected 16 items, but found {len(shop_items)}"

    def add_first_item_to_cart(self):
        self.do_click(self.first_add_button)
        time.sleep(5)

    def add_multiple_items_to_cart(self):
        album_item_price = float(self.get_element_text(self.album_item).replace('$', ''))
        beanie_item_price = float(self.get_element_text(self.beanie_item).replace('$', ''))
        beanie_with_logo_item_price = float(self.get_element_text(self.beanie_with_logo_item).replace('$', ''))
        belt_item_price = float(self.get_element_text(self.belt_item).replace('$', ''))

        self.items_total_price = round(album_item_price + beanie_item_price + beanie_with_logo_item_price + belt_item_price, 2)

        self.do_click(self.add_album_item)
        self.do_click(self.add_beanie_item)
        self.do_click(self.add_beanie_with_logo_item)
        self.do_click(self.add_belt_item)
        time.sleep(5)
