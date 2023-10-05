from selenium.webdriver.common.by import By
import allure

class CheckSuccessOrder():
    button_order = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    button_confirm = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    order = (By.CSS_SELECTOR, "div.Order_ModalHeader__3FDaJ")
    button_new_order = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']")

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Находим и нажимаем на кнопку заказать')
    def click_button_order(self):
        self.driver.find_element(*self.button_order).click()
    @allure.step('Подтверждаем заказ и нажимаем на кнопку "да"')
    def confirm_order(self):
        self.driver.find_element(*self.button_confirm).click()
    @allure.step('Проверяем успешность формирования заказа')
    def check_success(self):
        text_order = self.driver.find_element(*self.order)
        text = text_order.text

    def check_click_view_order(self):
        button = self.driver.find_element(*self.button_new_order)
        assert button.is_displayed() and button.is_enabled()
        button.click()

    def confirm_order(self):
        self.click_button_order()
        self.confirm_order()
        self.check_success()
        self.check_click_view_order()





