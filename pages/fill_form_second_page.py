from selenium.webdriver.common.by import By
from constants import *
import allure

class BasePage():
    def __init__(self, driver):
        self.driver = driver


    def click_element(self, locator):
        self.driver.find_element(*locator).click()


    def send_keys_to_element(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

class FillFormSecond(BasePage):
    date = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    date_def = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and contains(@class, 'react-datepicker__day--028') and contains(@class, 'react-datepicker__day--weekend') and starts-with(@aria-label, 'Choose суббота, 28-е октября 2023 г.')]")
    time = (By.XPATH, "//div[@class='Dropdown-control' and @aria-haspopup='listbox']//div[@class='Dropdown-placeholder'][text()='* Срок аренды']")
    time_def = (By.XPATH, "//div[@class='Dropdown-option' and @role='option' and @aria-selected='false' and text()='двое суток']")
    color = (By.XPATH, "//input[@id='black' and @class='Checkbox_Input__14A2w' and @type='checkbox']")
    comment = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    @allure.step('Находим поле даты доставки и выбираем дату')
    def fill_date(self):
        self.click_element(self.date)
        self.click_element(self.date_def)

    @allure.step('Находим поле срока аренды и выбираем срок')
    def fill_time(self):
        self.click_element(self.time)
        self.click_element(self.time_def)

    @allure.step('Находим поле выбора цвета и выбираем цвет')
    def fill_color(self):
        self.click_element(self.color)

    @allure.step('Находим поле комментария и вводим комментарий')
    def fill_comment(self, comment_text):
        self.send_keys_to_element(self.comment, comment_text)

    @allure.step("Заполняем форму заказа")
    def fill_form_order(self):
        self.fill_date()
        self.fill_time()
        self.fill_color()
        self.fill_comment(comment_form)
