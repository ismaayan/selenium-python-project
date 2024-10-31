from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class OrdersPage(BasePage):

    order_number_element = (By.CSS_SELECTOR, "td[class='woocommerce-orders-table__cell woocommerce-orders-table__cell-order-number'] a")
    order_date_element = (By.CSS_SELECTOR, ".woocommerce-orders-table__cell.woocommerce-orders-table__cell-order-date time")


    def __init__(self, driver):
        super().__init__(driver)

