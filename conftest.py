import pytest
import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver

@pytest.fixture(scope="function")
def driver():
    chrome_service = Service('chromedriver/chromedriver')
    driver = WebDriver(service=chrome_service)
    driver.maximize_window()
    yield driver
    driver.quit()

