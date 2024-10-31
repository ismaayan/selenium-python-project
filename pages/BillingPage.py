from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from pages.AccountPage import AccountPage
from pages.OrdersPage import  OrdersPage


class BillingPage(BasePage):

    billing_details = (By.CSS_SELECTOR, 'section.woocommerce-customer-details>address')
    order_number_element = (By.CSS_SELECTOR, 'li[class="woocommerce-order-overview__order order"] strong')
    order_date_element = (By.CSS_SELECTOR, 'li[class="woocommerce-order-overview__date date"] strong')


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


    def verify_order_history_in_user_account(self):
        account_page = AccountPage(self.driver)
        order_page = OrdersPage(self.driver)

        order_number = self.get_element_text(self.order_number_element)
        order_date = self.get_element_text(self.order_date_element)
        account_page.open_account_page()
        self.do_click(account_page.recent_orders_link)

        order_number_in_orders_page = self.get_element_text(order_page.order_number_element).replace("#", "")
        order_date_in_orders_page = self.get_element_text(order_page.order_date_element)

        assert order_number == order_number_in_orders_page, "order number isn't equal"
        assert  order_date == order_date_in_orders_page, "date isn't equal"






