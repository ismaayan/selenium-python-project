import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "http://demostore.supersqa.com/"


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Send 'chrome' or 'firefox' as parameter for execution"
    )
def navigate_to_demo_ecom_store(driver):
    driver.get(BASE_URL)
    return driver

@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    # Default driver value
    driver = ""
    # Option setup to run in headless mode (in order to run this in GH Actions)
    options = Options()
    # options.add_argument('--headless')
    # Setup
    print(f"\nSetting up: {browser} driver")
    if browser == "chrome":
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    # Implicit wait setup for our framework
    navigate_to_demo_ecom_store(driver)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    # Tear down
    print(f"\nTear down: {browser} driver")
    driver.quit()


