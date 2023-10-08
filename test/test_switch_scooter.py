from pages.click_logo_scooter import CheckLogoScooter
import allure
class TestSwitchScooter:
    @allure.description(
        'Переход по лого "Самокат"')
    def test_switch_scooter(self):

        order_page_logo_scooter = CheckLogoScooter(self.driver)
        order_page_logo_scooter.check_click_logo_scooter()

