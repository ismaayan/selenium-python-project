from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_in_checkout_form(self):
        wait = WebDriverWait(self.driver, 10)

        proceed_to_checkout_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Proceed to checkout')]"))
        )
        proceed_to_checkout_btn.click()

        first_name_field = self.driver.find_element(By.ID, 'billing_first_name')
        last_name_field = self.driver.find_element(By.ID, 'billing_last_name')
        first_name_field.send_keys("fakename")
        last_name_field.send_keys("fakelastname")

        country_dropdown = self.driver.find_element(By.ID, 'select2-billing_country-container')
        country_dropdown.click()

        france_option = self.driver.find_element(By.XPATH, "//li[contains(text(),'France')]")
        france_option.click()

        street_address_field = self.driver.find_element(By.ID, 'billing_address_1')
        street_address_field.send_keys('Rue de Rivoli')

        city_field = self.driver.find_element(By.ID, 'billing_city')
        city_field.send_keys('Paris')

        zipcode_field = self.driver.find_element(By.ID, 'billing_postcode')
        zipcode_field.send_keys('75001')

        phone_field = self.driver.find_element(By.ID, 'billing_phone')
        phone_field.send_keys('0123456789')

        place_order_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "place_order"))
        )
        place_order_btn.click()
