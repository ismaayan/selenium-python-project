import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_cart_page(self):
        self.driver.get("http://demostore.supersqa.com/cart")

    def add_first_item_to_cart(self):
        first_add_button = self.driver.find_element(By.CLASS_NAME, 'add_to_cart_button')
        first_add_button.click()

    def apply_coupon(self, coupon_code):
        coupon_field = self.driver.find_element(By.ID, 'coupon_code')
        apply_button = self.driver.find_element(By.CSS_SELECTOR,
            '#post-7 > div > div > form > table > tbody > tr:nth-child(2) > td > div > button')
        coupon_field.send_keys(coupon_code)
        apply_button.click()

    def verify_cart_has_item(self):
        for i in range(5):
            try:
                self.driver.find_element(By.CLASS_NAME, 'cart_item')
                return
            except NoSuchElementException:
                print('Item not in cart. Retrying after 2 seconds')
                time.sleep(2)
                self.driver.refresh()
        raise Exception("Item not found in cart after 5 retries")

    def verify_total_price(self, total_price):
        wait = WebDriverWait(self.driver, 10)
        total_price_field = wait.until(EC.visibility_of_element_located((
            By.CSS_SELECTOR,
            '#post-7 > div > div > div.cart-collaterals > div > table > tbody > tr.order-total > td > strong > span > bdi')))
        displayed_total = total_price_field.text.strip()

        if displayed_total == total_price:
            print(f"Total price verified: {displayed_total}")
        else:
            print(f"Total price mismatch: Expected {total_price}, but found {displayed_total}")

    def proceed_to_checkout(self):
        wait = WebDriverWait(self.driver, 10)
        proceed_to_checkout_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Proceed to checkout')]")))
        proceed_to_checkout_button.click()



