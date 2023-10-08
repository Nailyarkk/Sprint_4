from selenium.webdriver.common.by import By
import allure
from constants import *
from pages.base_page import BasePage

class CheckLogoScooter(BasePage):
    logo_scooter = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")

    @allure.step('Проверяем путь при нажатии на лого "Самокат"')
    def check_click_logo_scooter(self, driver):
        self.go_to_url(url)
        current_url = self.get_current_url()
        self.click_element(*self.logo_scooter)
        self.wait_for_url_change(current_url)
        new_url = self.get_current_url()
        assert new_url == url


