import time

from selenium.webdriver.common.by import By
from pages.AccountPage import AccountPage
from pages.BillingPage import BillingPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.HomePage import HomePage
from pages.ItemPage import ItemPage



def test_sanity_end_to_end(driver):
    account_page = AccountPage(driver)
    home_page = HomePage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    billing_page = BillingPage(driver)

    account_page.open_account_page()
    account_page.register_user_and_login()

    home_page.go_to_homepage()
    home_page.shop_item_count()
    home_page.add_first_item_to_cart()

    cart_page.go_to_cart_page()
    cart_page.apply_coupon('SSQA100')
    cart_page.verify_cart_has_item()
    time.sleep(3)
    cart_page.verify_total_price(0.00)

    checkout_page.fill_in_checkout_form()

    billing_page.verify_billing_details(account_page)
    billing_page.verify_order_history_in_user_account()



def test_multiple_items_total_price_sum_up(driver):
    home_page = HomePage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    home_page.add_multiple_items_to_cart()

    cart_page.go_to_cart_page()
    cart_page.verify_total_price(home_page.items_total_price)
    cart_page.proceed_to_checkout()

    checkout_page.verify_checkout_total_price(home_page.items_total_price)


def test_remove_item_from_cart(driver):
    home_page = HomePage(driver)
    cart_page = CartPage(driver)

    home_page.add_first_item_to_cart()
    cart_page.go_to_cart_page()
    cart_page.remove_item_from_cart()
    cart_page.verify_item_removed_from_cart()


def test_quantity_item_update(driver):
    cart_page = CartPage(driver)
    home_page = HomePage(driver)
    item_page = ItemPage(driver)

    home_page.enter_album_item_page()
    item_page.update_album_item_quantity_and_add_to_cart(3)
    cart_page.go_to_cart_page()
    cart_quantity = driver.find_element(By.CSS_SELECTOR, ".quantity input")
    assert cart_quantity.get_attribute("value") == "3"


def test_lost_password_link(driver):
    account_page = AccountPage(driver)

    account_page.open_account_page()
    account_page.verify_lost_password_page_opened()


def test_search_field(driver):
    home_page = HomePage(driver)

    home_page.verify_search_field('logo')


def test_homepage_header_and_footer(driver):
    home_page = HomePage(driver)

    home_page.verify_header()
    home_page.verify_footer()



















