from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.items_total_price = None

    def go_to_homepage(self):
        self.driver.get("http://demostore.supersqa.com/")
        self.driver.maximize_window()

    def shop_item_count(self):
        shop_items = self.driver.find_elements(By.CSS_SELECTOR, "#main ul li.product")
        assert len(shop_items) == 16, f"Expected 16 items, but found {len(shop_items)}"

    def add_first_item_to_cart(self):
        first_add_button = self.driver.find_element(By.CLASS_NAME, 'add_to_cart_button')
        first_add_button.click()

    def add_multiple_items_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        album_item = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li.post-24 bdi:nth-child(1)")))
        album_item_price = float(album_item.text.strip().replace('$', ''))
        beanie_item = self.driver.find_element(By.CSS_SELECTOR, "li.post-16 ins bdi:nth-child(1)")
        beanie_item_price = float(beanie_item.text.strip().replace('$', ''))
        beanie_with_logo_item = self.driver.find_element(By.CSS_SELECTOR, "li.post-33 ins bdi:nth-child(1)")
        beanie_with_logo_item_price = float(beanie_with_logo_item.text.strip().replace('$', ''))
        belt_item = self.driver.find_element(By.CSS_SELECTOR, "li.post-17 ins bdi:nth-child(1)")
        belt_item_price = float(belt_item.text.strip().replace('$', ''))

        self.items_total_price = album_item_price + beanie_item_price + beanie_with_logo_item_price + belt_item_price

        add_album_item = self.driver.find_element(By.XPATH, "//a[@aria-label='Add “Album” to your cart']")
        add_album_item.click()
        add_beanie_item = self.driver.find_element(By.XPATH, "//a[@aria-label='Add “Beanie” to your cart']")
        add_beanie_item.click()
        add_beanie_with_logo_item = self.driver.find_element(By.XPATH, "//a[@aria-label='Add “Beanie with Logo” to your cart']")
        add_beanie_with_logo_item.click()
        add_belt_item = self.driver.find_element(By.XPATH, "//a[@aria-label='Add “Belt” to your cart']")
        add_belt_item.click()
