from selenium.webdriver.common.by import By
import allure
from base_page import BasePage


class OrderScooterButton(BasePage):
    button_order1 = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    button_order2 = (
        By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM')]")

    @allure.step('Переходим на сайт')
    def go_to_url_main(self, url):
        self.go_to_url(url)

    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_button(self, button_order):
        self.click_element(button_order)
