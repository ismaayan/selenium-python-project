from faker import Faker
from selenium.webdriver.common.by import By

class AccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.random_email = None
        self.random_name = None

    def open_account_page(self):
        my_account = self.driver.find_element(By.XPATH, "//a[contains(text(), 'My account')]")
        my_account.click()
        self.driver.get("http://demostore.supersqa.com/my-account")

    def register_user_and_login(self):
        fake = Faker()
        self.random_name = fake.name().replace(" ", "").lower()
        self.random_email = self.random_name + "@gmail.com"

        register_email_field = self.driver.find_element(By.ID, "reg_email")
        register_password_field = self.driver.find_element(By.ID, "reg_password")
        register_btn = self.driver.find_element(By.NAME, 'register')

        register_email_field.send_keys(self.random_email)
        register_random_password = self.random_name + str(fake.random_number(digits=3))
        register_password_field.send_keys(register_random_password)
        register_btn.click()

        verify_registration_details = self.driver.find_element(By.XPATH, f"//strong[contains(text(), '{self.random_name}')]")
        verify_registration_details.is_displayed()

        logout_btn = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Log out')]")
        logout_btn.click()

        login_email_field = self.driver.find_element(By.ID, "username")
        login_password_field = self.driver.find_element(By.ID, "password")
        login_email_field.send_keys(self.random_email)
        login_password_field.send_keys(register_random_password)

        login_btn = self.driver.find_element(By.NAME, "login")
        login_btn.click()

        verify_registration_details = self.driver.find_element(By.XPATH, f"//strong[contains(text(), '{self.random_name}')]")
        verify_registration_details.is_displayed()

        print(self.random_name)
        print(register_random_password)
