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
    header_navbar = (By.CSS_SELECTOR, ".nav-menu li a")
    cart_icon = (By.CSS_SELECTOR, "a.cart-contents, .site-header-cart .widget_shopping_cart")
    header_price_field = (By.CSS_SELECTOR, "#site-header-cart a span")
    footer_text = (By.CLASS_NAME, "site-info")


    def __init__(self, driver):
        super().__init__(driver)
        self.items_total_price = None

    def go_to_homepage(self):
        self.driver.get("http://demostore.supersqa.com/")

    def shop_item_count(self):
        shop_items = self.driver.find_elements(By.CSS_SELECTOR, "#main ul li.product")
        assert len(shop_items) == 16, f"Expected 16 items, but found {len(shop_items)}"

    def add_first_item_to_cart(self):
        self.do_click(self.first_add_button)
        time.sleep(3)
        actual_items_count = self.get_element_text(self.cart_count_items)
        expected_items_count = "1 item"
        if actual_items_count != expected_items_count:
            print(f"Expected {expected_items_count}, but got {actual_items_count}")
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
        time.sleep(5)
        if actual_items_count != expected_items_count:
            print(f"Expected {expected_items_count} items, but got {actual_items_count}")
        else:
            pass

    def enter_album_item_page(self):
        self.do_click(self.album_product_link)

    def verify_search_field(self, key_word):
        self.do_send_keys(self.search_field, key_word)
        self.press_enter()

        # Get the list of search results
        items = self.driver.find_elements(By.CLASS_NAME, "woocommerce-loop-product__title")
        # verify 'logo' word exist in the items list results
        for item in items:
            items_text = item.text.lower()
            if "logo" not in items_text:
                print("Test Failed: 'logo' not found in the search results.")
            else:
                pass


    def verify_header(self):
        # Verify title
        self.get_title('Demo eCom Store – Just another WordPress site')
        # Verify search field
        self.is_enabled(self.search_field)
       # Verify navigation bar
        expected_header_links = ['Home', 'Cart', 'Checkout', 'My account', 'Sample Page']

        actual_header_links = self.driver.find_elements(By.CSS_SELECTOR, 'ul.nav-menu li a')

        # Extract the text from the found links
        actual_header_links_texts = [link.text for link in actual_header_links]

        # Verify each expected link is present in the header
        assert expected_header_links == actual_header_links_texts, (f"Expected header links : {expected_header_links}"
                                                                    f", but got '{actual_header_links_texts}'")

        # Verify cart elements
        expected_cart_default_price = '$0.00'
        # actual_cart_default_price = self.get_element_text(self.header_price_field)
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element
                                             (self.header_price_field, expected_cart_default_price))
        # assert actual_cart_default_price == expected_cart_default_price, (f"Expected text : {expected_cart_default_price}"
        #                                                                   f", but got '{actual_cart_default_price}'")


        expected_default_items_count = '0 items'
        actual_cart_default_items_count = self.get_element_text(self.cart_count_items)
        assert actual_cart_default_items_count == expected_default_items_count, (f"Expected text : {expected_default_items_count}"
                                                                                 f", but got '{actual_cart_default_items_count}'")

        self.is_enabled(self.cart_icon)


    def verify_footer(self):
        expected_footer_text = "© Demo eCom Store 2024\nBuilt with Storefront & WooCommerce."
        actual_footer_text = self.get_element_text(self.footer_text)

        assert actual_footer_text == expected_footer_text , f"Expected '{expected_footer_text}', but got '{actual_footer_text}'"




















