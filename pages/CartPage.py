import time
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage


class CartPage(BasePage):
    first_add_button = (By.CLASS_NAME, 'add_to_cart_button')
    coupon_field = (By.ID, 'coupon_code')
    apply_button = (By.CSS_SELECTOR, '#post-7 > div > div > form > table > tbody > tr:nth-child(2) > td > div > button')
    proceed_to_checkout_button = (By.XPATH, "//a[contains(text(), 'Proceed to checkout')]")
    total_price_field = (By.CSS_SELECTOR, "tr[class='order-total'] bdi:nth-child(1)")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_cart_page(self):
        self.driver.get("http://demostore.supersqa.com/cart")

    def add_first_item_to_cart(self):
        self.do_click(self.first_add_button)

    def apply_coupon(self, coupon_code):
        self.do_send_keys(self.coupon_field, coupon_code)
        self.do_click(self.apply_button)

    def verify_cart_has_item(self):
        for i in range(5):
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located
                                                     ((By.CLASS_NAME, 'cart_item')))
                return
            except NoSuchElementException:
                print('Item not in cart. Retrying after 2 seconds')
                time.sleep(2)
                self.driver.refresh()
        raise Exception("Item not found in cart after 5 retries")

    def verify_total_price(self, total_price):
        time.sleep(5)
        try:
            displayed_total_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.total_price_field)
            ).text

            displayed_total = round(float(displayed_total_text.replace('$', '')), 2)
            if displayed_total == round(total_price, 2):
                print(f"Total price verified: ${displayed_total:.2f}")
            else:
                print(f"Total price mismatch: Expected ${total_price:.2f}, but found ${displayed_total:.2f}")
        except TimeoutException:
            raise Exception("Failed to find total price element on the page")

    def proceed_to_checkout(self):
        self.do_click(self.proceed_to_checkout_button)



