from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BillingPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_billing_details(self, account_page):
        wait = WebDriverWait(self.driver, 10)
        billing_details = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'section.woocommerce-customer-details>address'))
        )

        displayed_billing_details = billing_details.text.strip()
        expected_details = (
            "fakename fakelastname\n"
            "Rue de Rivoli\n"
            "75001 PARIS\n"
            "France\n"
            "0123456789\n"
            f"{account_page.random_email}"
        )

        assert displayed_billing_details == expected_details, f"Text does not match: {displayed_billing_details}"

