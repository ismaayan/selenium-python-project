import pytest
from selenium import webdriver


BASE_URL = "http://demostore.supersqa.com/"


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    navigate_to_demo_ecom_store(driver)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    yield driver
    driver.quit()

def navigate_to_demo_ecom_store(driver):
    driver.get(BASE_URL)
    return driver