import pytest
from selenium import webdriver
from pages.account_page import AccountPage
from pages.billing_page import BillingPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


def test_sanity_end_to_end(driver):
    driver.get("http://demostore.supersqa.com/")
    driver.maximize_window()
    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.register_user_and_login()

    home_page = HomePage(driver)
    home_page.go_to_homepage()
    home_page.shop_item_count()
    home_page.add_first_item_to_cart()

    cart_page = CartPage(driver)
    cart_page.go_to_cart_page()
    cart_page.apply_coupon('SSQA100')
    cart_page.verify_cart_has_item()
    cart_page.verify_total_price('0.00')

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_in_checkout_form()

    billing_page = BillingPage(driver)
    billing_page.verify_billing_details(account_page)

def test_multiple_items_total_price_sum_up(driver):
    driver.get("http://demostore.supersqa.com/")
    driver.maximize_window()
    home_page = HomePage(driver)
    home_page.add_multiple_items_to_cart()
    cart_page = CartPage(driver)
    cart_page.go_to_cart_page()
    cart_page.verify_total_price(home_page.items_total_price)
    cart_page.proceed_to_checkout()
    checkout_page = CheckoutPage(driver)
    checkout_page.verify_checkout_total_price(home_page.items_total_price)




