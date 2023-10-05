from selenium.webdriver.common.by import By
import allure

class OrderScooterButton():
    button_order1 = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    button_order2 = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM')]")

    def __init__(self, driver):
        self.driver = driver
    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_button(self, button_order):
        self.driver.find_element(button_order).click()



