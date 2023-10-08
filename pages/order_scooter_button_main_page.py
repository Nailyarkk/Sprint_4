from selenium.webdriver.common.by import By
import allure


class BasePage():
    def __init__(self, driver):
        self.driver = driver


    def click_element(self, locator):
        self.driver.find_element(*locator).click()


class OrderScooterButton(BasePage):
    button_order1 = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    button_order2 = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM')]")

    @allure.step('Нажимаем на кнопку "Заказать"')
    def click_button(self, button_order):
        self.click_element(button_order)



