from selenium.webdriver.common.by import By
import allure
from base_page import BasePage
from constants import success_text


class CheckSuccessOrder(BasePage):
    button_order = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    button_confirm = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    order = (By.CSS_SELECTOR, "div.Order_ModalHeader__3FDaJ")
    button_new_order = (
        By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']")

    @allure.step('Находим и нажимаем на кнопку заказать')
    def click_button_order(self):
        self.click_element(self.button_order)

    @allure.step('Подтверждаем заказ и нажимаем на кнопку "да"')
    def confirm_order(self):
        self.click_element(self.button_confirm)

    @allure.step('Проверяем успешность формирования заказа')
    def check_success(self):
        text = self.get_element_text(self.order)
        return text

    @allure.step('Находим и нажимаем на кнопку перехода сформировавшегося заказа')
    def check_click_view_order(self):
        self.click_element(self.button_new_order)

    @allure.step('Проверка успешности формирования заказа')
    def complete_order_process(self):
        self.click_button_order()
        self.confirm_order()
        order_status = self.check_success()
        self.check_click_view_order()
        assert order_status == success_text
