from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.BasePage import BasePage


class CheckoutPage(BasePage):
    proceed_to_checkout_btn = (By.XPATH, "//a[contains(text(),'Proceed to checkout')]")
    first_name_field = (By.ID, 'billing_first_name')
    last_name_field = (By.ID, 'billing_last_name')
    country_dropdown = (By.ID, 'select2-billing_country-container')
    france_country_option = (By.XPATH, "//li[contains(text(),'France')]")
    street_address_field = (By.ID, 'billing_address_1')
    city_field = (By.ID, 'billing_city')
    zipcode_field = (By.ID, 'billing_postcode')
    phone_field = (By.ID, 'billing_phone')
    place_order_btn = (By.ID, "place_order")
    total_price_field = (By.CSS_SELECTOR,"tr[class='order-total'] bdi:nth-child(1)")
    checkout_product_quantity = (By.CSS_SELECTOR, ".product-quantity")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_in_checkout_form(self):
        self.do_click(self.proceed_to_checkout_btn)
        self.do_send_keys(self.first_name_field, "fakename")
        self.do_send_keys(self.last_name_field, "fakelastname")

        self.do_click(self.country_dropdown)
        self.do_click(self.france_country_option)

        self.do_send_keys(self.street_address_field, 'Rue de Rivoli')
        self.do_send_keys(self.city_field, 'Paris')
        self.do_send_keys(self.zipcode_field, '75001')
        self.do_send_keys(self.phone_field, '0123456789')

        self.do_click(self.place_order_btn)

    def verify_checkout_total_price(self, total_price):
        try:
            displayed_total_text = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.total_price_field)
            ).text

            displayed_total = round(float(displayed_total_text.replace('$', '').replace(',', '')), 2)
            if displayed_total != round(total_price, 2):
                print(f"Total price mismatch: Expected ${total_price:.2f}, but found ${displayed_total:.2f}")
            else:
                pass
        except TimeoutException:
            raise Exception("Failed to find total price element on the page")




