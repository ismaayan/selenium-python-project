from faker import Faker
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class AccountPage(BasePage):

    register_email_field = (By.ID, "reg_email")
    register_password_field = (By.ID, "reg_password")
    register_btn = (By.NAME, 'register')
    logout_btn = (By.XPATH, "//a[contains(text(), 'Log out')]")
    login_email_field = (By.ID, "username")
    login_password_field = (By.ID, "password")
    login_btn = (By.NAME, "login")
    lost_password_link = (By.XPATH, "//a[contains(text(), 'Lost your password?')]")
    username_or_email_input = (By.ID, "user_login")
    reset_password_button = (By.XPATH, "//button[contains(text(), 'Reset password')]")
    recent_orders_link = (By.LINK_TEXT, 'recent orders')


    def __init__(self, driver):
        super().__init__(driver)
        self.fake = Faker()
        self.random_email = None
        self.random_name = None

    def open_account_page(self):
        self.driver.get("http://demostore.supersqa.com/my-account")

    def register_user_and_login(self):
        self.random_name = self.fake.name().replace(" ", "").lower()
        self.random_email = self.random_name + "@gmail.com"
        self.do_send_keys(self.register_email_field, self.random_email)
        register_random_password = self.random_name + str(self.fake.random_number(digits=3))
        self.do_send_keys(self.register_password_field,register_random_password)
        self.do_click(self.register_btn)

        assert self.driver.find_element(By.XPATH, f"//strong[contains(text(), '{self.random_name}')]").is_displayed

        self.do_click(self.logout_btn)

        self.do_send_keys(self.login_email_field, self.random_email)
        self.do_send_keys(self.login_password_field,register_random_password)

        self.do_click(self.login_btn)

        assert self.driver.find_element(By.XPATH, f"//strong[contains(text(), '{self.random_name}')]").is_displayed()

    def verify_lost_password_page_opened(self):
      self.do_click(self.lost_password_link)
      current_url = self.driver.current_url
      expected_url = "http://demostore.supersqa.com/my-account/lost-password/"

      # Assert to check if the page opened
      assert current_url == expected_url, f"Expected {expected_url}, but got {current_url}"
      # Verify username or email input field exist
      try:
          self.is_enabled(self.username_or_email_input)
      except NoSuchElementException:
            print("Username or email input field does not exist.")

      # Verify reset password button exist
      try:
          self.is_enabled(self.reset_password_button)
      except NoSuchElementException:
          print("Reset password button does not exist.")





