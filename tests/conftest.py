import pytest
from selenium import webdriver


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

    # Setup
    print(f"\nSetting up: {browser} driver")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-debugging-port=9222")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Firefox(options=options)
    # Implicit wait setup for our framework
    navigate_to_demo_ecom_store(driver)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    # Tear down
    print(f"\nTear down: {browser} driver")
    driver.quit()


