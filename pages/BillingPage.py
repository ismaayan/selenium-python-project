from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class BillingPage(BasePage):

    billing_details = (By.CSS_SELECTOR, 'section.woocommerce-customer-details>address')

    def __init__(self, driver):
        super().__init__(driver)

    def verify_billing_details(self, account_page):
        displayed_billing_details = self.get_element_text(self.billing_details)
        expected_details = (
            "fakename fakelastname\n"
            "Rue de Rivoli\n"
            "75001 PARIS\n"
            "France\n"
            "0123456789\n"
            f"{account_page.random_email}"
        )

        assert displayed_billing_details == expected_details, f"Text does not match: {displayed_billing_details}"

