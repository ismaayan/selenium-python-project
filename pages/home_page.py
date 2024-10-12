from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_homepage(self):
        self.driver.get("http://demostore.supersqa.com/")
        self.driver.maximize_window()

    def shop_item_count(self):
        shop_items = self.driver.find_elements(By.CSS_SELECTOR, "#main ul li.product")
        assert len(shop_items) == 16, f"Expected 16 items, but found {len(shop_items)}"

    def add_first_item_to_cart(self):
        first_add_button = self.driver.find_element(By.CLASS_NAME, 'add_to_cart_button')
        first_add_button.click()
