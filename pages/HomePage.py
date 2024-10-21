import time
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    first_add_button = (By.LINK_TEXT, 'Add to cart')
    album_item = (By.CSS_SELECTOR, "li.post-24 bdi:nth-child(1)")
    beanie_item = (By.CSS_SELECTOR, "li.post-16 ins bdi:nth-child(1)")
    beanie_with_logo_item = (By.CSS_SELECTOR, "li.post-33 ins bdi:nth-child(1)")
    belt_item = (By.CSS_SELECTOR, "li.post-17 ins bdi:nth-child(1)")
    add_album_item = (By.XPATH, "//a[@aria-label='Add “Album” to your cart']")
    add_beanie_item = (By.XPATH, "//a[@aria-label='Add “Beanie” to your cart']")
    add_beanie_with_logo_item = (By.XPATH, "//a[@aria-label='Add “Beanie with Logo” to your cart']")
    add_belt_item = (By.XPATH, "//a[@aria-label='Add “Belt” to your cart']")
    cart_count_items = (By.XPATH, "//a[@class='cart-contents']/span[2]")
    album_product_link = (By.XPATH, "//h2[contains(text(), 'Album')]")
    add_to_cart_button = (By.NAME, "add-to-cart")
    search_field = (By.ID, "woocommerce-product-search-field-0")
    items_list = (By.CSS_SELECTOR, "self.products.columns-4 li")


    def __init__(self, driver):
        super().__init__(driver)
        self.items_total_price = None

    def shop_item_count(self):
        shop_items = self.driver.find_elements(By.CSS_SELECTOR, "#main ul li.product")
        assert len(shop_items) == 16, f"Expected 16 items, but found {len(shop_items)}"

    def add_first_item_to_cart(self):
        self.do_click(self.first_add_button)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                             (self.cart_count_items))
        actual_items_count = self.get_element_text(self.cart_count_items)
        expected_items_count = "1 item"
        if actual_items_count != expected_items_count:
            print(f"Expected {expected_items_count} items, but got {actual_items_count}")
        else:
            pass

    def get_prices(self):
        album_price = float(self.get_element_text(self.album_item).replace('$', ''))
        beanie_price = float(self.get_element_text(self.beanie_item).replace('$', ''))
        beanie_logo_price = float(self.get_element_text(self.beanie_with_logo_item).replace('$', ''))
        belt_price = float(self.get_element_text(self.belt_item).replace('$', ''))
        return album_price, beanie_price, beanie_logo_price, belt_price

    def add_multiple_items_to_cart(self):
        album_price, beanie_price, beanie_logo_price, belt_price = self.get_prices()
        self.items_total_price = round(album_price + beanie_price + beanie_logo_price + belt_price, 2)

        self.do_click(self.add_album_item)
        self.do_click(self.add_beanie_item)
        self.do_click(self.add_beanie_with_logo_item)
        self.do_click(self.add_belt_item)
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                             (self.cart_count_items))
        actual_items_count = self.get_element_text(self.cart_count_items)
        expected_items_count = "4 items"
        if actual_items_count != expected_items_count:
            print(f"Expected {expected_items_count} items, but got {actual_items_count}")
        else:
            pass

    def enter_album_item_page(self):
        self.do_click(self.album_product_link)

    def verify_search_field(self, key_word):
        self.do_send_keys(self.search_field, key_word)
        items = self.items_list
        items_list = []
        for item in items:
            self.get_element_text(item)
            items_list.append(item)
        for item in items_list:
            if key_word in item.text:
                print("Text is present in the element")
            else:
                print("Text is NOT present in the element")









