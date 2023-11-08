from selenium.webdriver.common.by import By
import allure
from constants import *
from pages.base_page import BasePage


class CheckLogoYandex(BasePage):
    logo_yandex = (By.CSS_SELECTOR, "a[href*='yandex']")

    @allure.step('Находим и нажимаем на лого "Яндекс"')
    def click_logo(self):
        self.click_element(self.logo_yandex)

    @allure.step('Проверяем переход на главную страницу Яндекса"')
    def check_click_logo_yandex(self):
        self.go_to_url(url)
        self.click_logo()
        self.switch_to_new_window()
        current_url = self.get_current_url()
        assert current_url == yandex_main
