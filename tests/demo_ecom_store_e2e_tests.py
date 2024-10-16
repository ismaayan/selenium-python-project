import pytest
from selenium import webdriver
from pages.AccountPage import AccountPage
from pages.BillingPage import BillingPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.HomePage import HomePage

BASE_URL = "http://demostore.supersqa.com/"


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def navigate_to_demo_ecom_store(driver):
    driver.get(BASE_URL)
    return driver


def test_sanity_end_to_end(driver):
    account_page = AccountPage(driver)
    home_page = HomePage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    billing_page = BillingPage(driver)

    navigate_to_demo_ecom_store(driver)
    driver.maximize_window()

    account_page.open_account_page()
    account_page.register_user_and_login()

    navigate_to_demo_ecom_store(driver)
    home_page.shop_item_count()
    home_page.add_first_item_to_cart()

    cart_page.go_to_cart_page()
    cart_page.apply_coupon('SSQA100')
    cart_page.verify_cart_has_item()
    cart_page.verify_total_price(0.00)

    checkout_page.fill_in_checkout_form()

    billing_page.verify_billing_details(account_page)


def test_multiple_items_total_price_sum_up(driver):
    home_page = HomePage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    navigate_to_demo_ecom_store(driver)
    driver.maximize_window()
    home_page.add_multiple_items_to_cart()


    cart_page.go_to_cart_page()
    cart_page.verify_total_price(home_page.items_total_price)
    cart_page.proceed_to_checkout()

    checkout_page.verify_checkout_total_price(home_page.items_total_price)

def test_remove_item_from_cart(driver):
    home_page = HomePage(driver)
    navigate_to_demo_ecom_store(driver)
    home_page.add_first_item_to_cart()
    cart_page = CartPage(driver)
    cart_page.go_to_cart_page()
    cart_page.remove_item_from_cart()
    cart_page.verify_item_removed_from_cart()
