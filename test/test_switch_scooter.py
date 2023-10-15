from pages.click_logo_yandex import CheckLogoYandex
from pages.click_logo_scooter import CheckLogoScooter
from constants import *
import allure
class TestSwitchScooter:
    @allure.description(
        'Переход по лого "Самокат"')
    def test_switch_scooter(self):
        self.driver.get(url)

        order_page_logo_scooter = CheckLogoScooter(self.driver)
        order_page_logo_scooter.check_click_logo_scooter()

