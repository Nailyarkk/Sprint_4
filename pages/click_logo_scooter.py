from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


from constants import *

class CheckLogoScooter():
    logo_scooter = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR' and @href='/']")
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Проверяем путь при нажатии на лого "Самокат"')
    def check_click_logo_scooter(self):
        current_url = self.driver.current_url
        self.driver.find_element(*self.logo_scooter).click()
        WebDriverWait(self.driver, 10).until(EC.url_changes(current_url))
        new_url = self.driver.current_url

        assert new_url == url




