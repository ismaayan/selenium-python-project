import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.usefixtures("init_driver")
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def is_element_absent(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(by_locator)
            )
            if element.is_displayed():
                print("Element shouldn't appear but it does")
                return False  # Element is present and visible

        except TimeoutException:
            return True

    def clear_text(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).clear()


    def press_enter(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ENTER).perform()








