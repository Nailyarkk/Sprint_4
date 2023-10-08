from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from constants import *

class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def wait_for_url_change(self, current_url):
        WebDriverWait(self.driver, 10).until(EC.url_changes(current_url))

class CheckLogoScooter(BasePage):
    logo_scooter = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")

    @allure.step('Проверяем путь при нажатии на лого "Самокат"')
    def check_click_logo_scooter(self):
        current_url = self.get_current_url()
        self.find_element(self.logo_scooter).click()
        self.wait_for_url_change(current_url)
        new_url = self.get_current_url()
        assert new_url == url




