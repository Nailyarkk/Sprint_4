from pages.click_logo_yandex import CheckLogoYandex
import allure


class TestSwitchScooter:
    @allure.description(
        'Переход по лого "Яндекс"')
    def test_switch_scooter(self):
        order_page_logo_yandex = CheckLogoYandex(self)
        order_page_logo_yandex.check_click_logo_yandex()
